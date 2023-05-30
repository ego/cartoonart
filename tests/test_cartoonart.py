import tempfile
from pathlib import Path

from typer.testing import CliRunner

from cartoonart.cli import app

runner = CliRunner()


def test_app():
    """CLI tests"""
    # https://typer.tiangolo.com/tutorial/testing/

    tmp = tempfile.gettempdir()
    file_pathi = Path("img/shuttle.jpg")
    file_patho = Path(f"{tmp}/cartoon-shuttle.jpg")
    python_cartoonart_cli_args = f"image --i {file_pathi} --o {file_patho}".split()
    result = runner.invoke(app, python_cartoonart_cli_args)
    assert result.exit_code == 0
    assert file_patho.exists()
