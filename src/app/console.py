"""Command-line interface."""
import textwrap

import click

from trading import pipeline

from . import __version__
from . import wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Return a random wikipedia page."""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))

    click.secho("Pipeline run", fg="red")
    data = pipeline.run()
    click.echo(data.head())
