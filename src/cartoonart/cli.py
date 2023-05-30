"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = cartoonart.cli:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import logging
from pathlib import Path
from typing import Optional

import cv2
import typer
from rich import print

from cartoonart import __version__
from cartoonart.image_processor import create_cartoon_art
from cartoonart.video_processor import create_video_art

__author__ = "Alter Ego"
__copyright__ = "Alter Ego"
__license__ = "MIT"
__app_name__ = "cartoonart"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


ERROR_I = "[bold magenta]Empty args: [/bold magenta][bold cyan]--i[/bold cyan]"
ERROR_O = "[bold magenta]Empty args: [/bold magenta][bold cyan]--o[/bold cyan]"

IMG_IPATH = typer.Option(
    None, exists=True, file_okay=True, readable=True, resolve_path=True
)
IMG_OPATH = typer.Option(None, file_okay=True)
VIDEO_OPATH = typer.Option(
    "video-art.avi",
    file_okay=True,
    help="Pass only directory, file will be named as video-art.avi",
)


app = typer.Typer()


def show_version(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def image(i: Path = IMG_IPATH, o: Path = IMG_OPATH):
    if i is None:
        print(ERROR_I)
        raise typer.Abort()

    image_path = cv2.imread(str(i))
    image_output = create_cartoon_art(image_path)

    if not o:
        o = Path(i.parent, f"cartoon-{i.stem}{i.suffix}")

    cv2.imwrite(str(o), image_output)
    print(f"Cartoon art was saved to {o}")


@app.command()
def video(o: Path = VIDEO_OPATH):
    if o is None:
        print(ERROR_O)
        raise typer.Abort()

    video_output = create_video_art(o)
    print(f"Cartoon video art was saved to {video_output}")


@app.callback()
def main(
    version: Optional[bool] = typer.Option(  # noqa: B008
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=show_version,
        is_eager=True,
    )
) -> None:
    return


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    app(prog_name=__app_name__)


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m cartoonart.cli image --i img/shuttle.jpg --o cartoon-shuttle.jpg
    #
    #
    run()
