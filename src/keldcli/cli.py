# -*- coding: utf-8 -*-

"""Command line interface implementation for the package."""

import click

from .__about__ import __title__, __version__


@click.group(invoke_without_command=True)
def cli():
    """Entry point for the console script."""
    click.echo('{} {}'.format(__title__, __version__))
