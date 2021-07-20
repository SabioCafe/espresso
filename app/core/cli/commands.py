"""Commands module."""
from os import environ

import click


@click.command("hello")
@click.option("--name", default="you", help="Your name.")
def greet(name):
    """A greet function."""
    print(f"Hello {name}, welcome! I'm {environ.get('APP_QUEUE', 'espresso')}.")
