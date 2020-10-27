from dbks.cli import cli
import click


@click.group()
def cli():
    """Commands for Databricks cluster operations."""
    pass


@cli.command()
@click.option(
    "-yml",
    "--yml-file",
    "yml_path",
    type=str,
    help="Absolute path of YAML file for cluster definitions.",
)
def create_or_edit(yml_path):
    """\b
    Parse a YAML file and use its content to create or edit cluster(s).
    Please refer to documentation for YAML file example.
    """
    click.echo(yml_path)
