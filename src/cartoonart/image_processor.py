from collections import defaultdict
from typing import Dict, List, Set, Tuple

import cv2
import numpy as np
from scipy import stats

K_MEANS_CLUSTERING_ALPHA = 0.001
K_MEANS_CLUSTERING_MIN_GROUP_SIZE = 80
K_MEANS_CLUSTERING_CENTERS_SIZE = 128


def create_cartoon_art(image: np.ndarray) -> np.ndarray:
    kernel = np.ones((2, 2), np.uint8)
    output = np.array(image)
    height, width, channels = output.shape

    # Apply bilateral filter to each channel
    for i in range(channels):
        output[:, :, i] = cv2.bilateralFilter(output[:, :, i], 5, 150, 150)

    # Apply edge detection using Canny
    edge = cv2.Canny(output, 100, 200)

    # Convert output to HSV color space
    output = cv2.cvtColor(output, cv2.COLOR_RGB2HSV)

    # Calculate histograms for each channel
    histograms: List[np.ndarray] = []
    for i in range(channels):
        hist, _ = np.histogram(output[:, :, i], bins=np.arange(256 + 1))
        histograms.append(hist)

    # Detect outliers in each histogram to determine color centers
    color_centers: List[np.ndarray] = []
    for hist in histograms:
        color_centers.append(detect_outliers(hist))

    # Reshape output for easier processing
    output = output.reshape((-1, channels))

    # Replace pixel values with color centers
    for i in range(channels):
        channel = output[:, i]
        index = np.argmin(np.abs(channel[:, np.newaxis] - color_centers[i]), axis=1)
        output[:, i] = color_centers[i][index]

    # Reshape output back to original shape
    output = output.reshape((height, width, channels))

    # Convert output back to RGB color space
    output = cv2.cvtColor(output, cv2.COLOR_HSV2RGB)

    # Find and draw contours on the edge image
    contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(output, contours, -1, 0, thickness=1)

    # Apply erosion to each channel
    for i in range(channels):
        output[:, :, i] = cv2.erode(output[:, :, i], kernel, iterations=1)

    return output


def detect_outliers(hist: np.ndarray) -> np.ndarray:
    # Initialize the centers with a single value
    centers = np.array([K_MEANS_CLUSTERING_CENTERS_SIZE])

    while True:
        # Update the centers based on the current histogram
        centers, groups = update_centers(centers, hist)

        # Create a set to store the new centers
        new_centers: Set[float] = set()
        for index, indices in groups.items():
            if len(indices) < K_MEANS_CLUSTERING_MIN_GROUP_SIZE:
                new_centers.add(centers[index])
                continue

            # Perform normality test on the histogram subset
            z_score, p_value = stats.normaltest(hist[indices])

            # Check if the subset is significantly different from a normal distribution
            if p_value < K_MEANS_CLUSTERING_ALPHA:
                left = 0 if index == 0 else centers[index - 1]
                right = (
                    len(hist) - 1 if index == len(centers) - 1 else centers[index + 1]
                )
                delta = right - left

                # Check if there is enough separation to split the cluster
                if delta >= 3:
                    center1 = (centers[index] + left) / 2
                    center2 = (centers[index] + right) / 2
                    new_centers.add(center1)
                    new_centers.add(center2)
                else:
                    new_centers.add(centers[index])
            else:
                new_centers.add(centers[index])

        # Check if the new centers have converged
        if len(new_centers) == len(centers):
            break
        else:
            centers = np.array(sorted(new_centers))

    return centers


def update_centers(
    centers: np.ndarray, histogram: np.ndarray
) -> Tuple[np.ndarray, Dict[int, List[int]]]:
    # Iterate until the centers converge
    while True:
        # Create groups to store indices based on the closest center
        groups: Dict[int, List[int]] = defaultdict(list)

        # Assign indices to the closest center
        for i, count in enumerate(histogram):
            if count == 0:
                continue
            distances = np.abs(centers - i)
            closest_index = np.argmin(distances)
            groups[closest_index].append(i)

        # Update the centers based on the grouped indices
        new_centers = centers.copy()
        for index, indices in groups.items():
            if np.sum(histogram[indices]) == 0:
                continue
            new_centers[index] = int(
                np.sum(indices * histogram[indices]) / np.sum(histogram[indices])
            )

        # Check if the centers have converged
        if np.sum(new_centers - centers) == 0:
            break
        centers = new_centers

    return centers, groups
