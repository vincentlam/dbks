from dbks.cli import cli
import click


@click.group()
def cli():
    """Commands for Databricks permission operations."""
    pass


@cli.command()
def replace_permission():
    pass
