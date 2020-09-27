# src/hypermodern_python/console.py
import textwrap


import click
import requests
import locale

# from hypermodern_python import __version__
from . import __version__


@click.command()
@click.option('--lang', default=locale.getlocale()[0][:2], help='Language setting')
@click.version_option(version=__version__)
def main(lang: str):
    API_URL = f"https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"

    """ The hypermodern python project """
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()
    except requests.exceptions.RequestException as e:
        click.secho("Whoops. This did not work.", fg="red")
        raise SystemExit(e)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))