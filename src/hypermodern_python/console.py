# src/hypermodern_python/console.py
import locale
import textwrap

import click

# from hypermodern_python import __version__
from . import __version__, wikipedia


def get_locale() -> str:

    return locale.getlocale()[0][:2] or "en"


@click.command()
@click.option(
    "--language",
    "-l",
    default=get_locale(),
    metavar="LANG",
    help="Language setting of Wikipedia",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str):
    """ The hypermodern python project """
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
