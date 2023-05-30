from pathlib import Path

import cv2
import numpy as np

from cartoonart.image_processor import create_cartoon_art


def create_video_art(video_output: Path) -> str:
    # Open the video capture device

    print("To stop video recording press `Q` key. ")

    video = cv2.VideoCapture(0)

    # Get the frame dimensions
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)

    # Define the output file path
    video_output.mkdir(parents=True, exist_ok=True)
    file_path = f"{video_output}/video-art.avi"

    # Create a video writer to save the output frames to a video file
    out = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*"MJPG"), 10, size)

    while True:
        # Read a frame from the video capture device
        ret, img = video.read()

        if not ret:
            # Break the loop if no frame is retrieved
            break

        # Create cartoon art from the frame
        img = create_cartoon_art(img)

        # Display the original frame
        cv2.imshow("original", np.array(img))

        # Write the cartoonized frame to the output video file
        out.write(img)

        # Check if the 'q' key is pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Got exit Q key, stopping ...")
            break

    # Release the video capture device and the video writer
    video.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    # Return the file path of the output video file
    return file_path
