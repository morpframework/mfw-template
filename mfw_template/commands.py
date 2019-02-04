from cookiecutter.main import cookiecutter
from .cli import project
import click
from pkg_resources import resource_filename
import os
import yaml


@project.command()
def create_project():
    cookiecutter(resource_filename('morpcookiecutter', 'templates/project'))


@project.command()
@click.pass_context
def create_resource(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('morpcookiecutter', 'templates/resource'),
                 output_dir=project_name)
