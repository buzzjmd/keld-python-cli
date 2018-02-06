# -*- coding: utf-8 -*-

"""Command line interface for the `kelcli` package."""

import click


@click.group(invoke_without_command=True)
def cli():
    click.echo('Keld Command Line Interface!')
