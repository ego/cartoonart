# Cartoon Art [![](https://img.shields.io/github/v/release/ego/cartoonart.svg?colorB=58839b)](https://github.com/ego/cartoonart/releases) [![PyPI](https://img.shields.io/pypi/v/cartoonart.svg)](https://pypi.org/project/cartoonart/)


> Create **cartoon** from image or video.

CLI tools for creating nice cartoon **images** and **video**.

![The output nature cartoon](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-nature.jpeg)
![The input nature image](https://raw.githubusercontent.com/ego/cartoonart/main/img/nature.jpeg)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/)

[![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg)](https://www.python.org/downloads/release/python-3100/)

[![Python 3.11](https://img.shields.io/badge/python-3.11-green.svg)](https://www.python.org/downloads/release/python-3110/)

### Install

```shell
pip install cartoonart
```

## How to use cartoonart

### Create cartoon art from image


```shell
cartoonart image --i img/nature.jpeg
cartoonart image --i img/nature.jpeg --o img/cartoon-nature.jpeg
cartoonart image --i img/shuttle.jpg --o img/cartoon-shuttle.jpg
```

You can omit option `--o` then cartoon will be saved with prefix `cartoon-`.

### Create cartoon art from video camera

```shell
cartoonart video
cartoonart video --o video
```

To stop video recording press `Q` key.

You can omit option `--o` then video will be saved as `video-art.avi`.

### Get help

```shell
cartoonart --help
cartoonart image --help
```

Install `cartoonart` CLI completion

```shell
cartoonart --show-completion
cartoonart --install-completion
```

## Cartoons gallery

![Morty](https://raw.githubusercontent.com/ego/cartoonart/main/img/morty.jpg)
![Cartoon Morty](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-morty.jpg)

![Rick and Morty](https://raw.githubusercontent.com/ego/cartoonart/main/img/rick-and-morty.jpg)
![Cartoon Rick and Morty](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-rick-and-morty.jpg)

![Shuttle](https://raw.githubusercontent.com/ego/cartoonart/main/img/shuttle.jpg)
![Cartoon shuttle](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-shuttle.jpg)

![Space](https://raw.githubusercontent.com/ego/cartoonart/main/img/space.jpg)
![Cartoon space](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-space.jpg)

![Star](https://raw.githubusercontent.com/ego/cartoonart/main/img/star.jpg)
![Cartoon star](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-star.jpg)

![Wormhole](https://raw.githubusercontent.com/ego/cartoonart/main/img/wormhole.jpg)
![Cartoon wormhole](https://raw.githubusercontent.com/ego/cartoonart/main/img/cartoon-wormhole.jpg)


## Contributing

[CONTRIBUTING](CONTRIBUTING.md)


## Stats

[![Monthly downloads](https://pepy.tech/badge/cartoonart/month)](https://pepy.tech/project/cartoonart)
