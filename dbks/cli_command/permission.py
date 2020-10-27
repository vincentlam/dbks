import click
import yaml
from dbks.cluster.controller import ClusterController
from dbks.permission.controller import PermissionController


cluster_ctl = ClusterController()
permission_ctl = PermissionController()


@click.group()
def cli():
    """Commands for Databricks permission operations."""
    pass


@cli.command()
@click.argument("cluster_id")
def get_cluster_permissions(cluster_id):
    permission_ctl.get_cluster_permissions(cluster_id)


@cli.command()
@click.argument("yml_path", type=click.Path(exists=True))
def replace_cluster_permissions_from_yml(yml_path):
    """\b
    Parse a YAML file and use its content to replace cluster permissions.
    Please refer to documentation for YAML file example.
    """
    with open(yml_path) as file:
        target_permissions = yaml.load(file, Loader=yaml.FullLoader)
    for cluster_name, permissions in target_permissions.items():
        cluster_id = cluster_ctl.get_id_by_name(cluster_name)[0]
        permission_ctl.replace_cluster_permissions(cluster_id, permissions)
