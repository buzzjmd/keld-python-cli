# -*- coding: utf-8 -*-

"""Command line interface implementation for the package."""

import click


@click.group(invoke_without_command=True)
def cli():
    """Entry point for the console script."""
    click.echo('Command Line Interface!')
