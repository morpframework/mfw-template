from cookiecutter.main import cookiecutter
from .cli import project
import click
from pkg_resources import resource_filename
import os
import yaml
from cryptography.fernet import Fernet

@project.command(help='create a new MorpFW project')
def create_project():
    cookiecutter(resource_filename('mfw_template', 'templates/project'),
            extra_context={
                'fernet_key': Fernet.generate_key().decode('utf-8')
            })


@project.command(help='create a new resource type')
@click.pass_context
def create_resource(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('mfw_template', 'templates/resource'),
                 extra_context={
        'project_name': project_name,
        'project_type': ctx.obj['RC']['project_type']},
        output_dir=project_name)


@project.command(help='create a new Application Behavior')
@click.pass_context
def create_applicationbehavior(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('mfw_template',
        'templates/applicationbehavior'),
                 extra_context={
        'project_name': project_name,
        'project_type': ctx.obj['RC']['project_type']},
        output_dir=project_name)


@project.command(help='create a new Entity Behavior')
@click.pass_context
def create_behavior(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('mfw_template',
        'templates/behavior'),
                 extra_context={
        'project_name': project_name,
        'project_type': ctx.obj['RC']['project_type']},
        output_dir=project_name)


@project.command(help='create a new Field Validator')
@click.pass_context
def create_fieldvalidator(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('mfw_template',
        'templates/fieldvalidator'),
                 extra_context={
        'project_name': project_name,
        'project_type': ctx.obj['RC']['project_type']},
        output_dir=project_name)


@project.command(help='create a new Form Validator')
@click.pass_context
def create_formvalidator(ctx):
    project_name = ctx.obj['RC']['project_name']
    cookiecutter(resource_filename('mfw_template',
        'templates/formvalidator'),
                 extra_context={
        'project_name': project_name,
        'project_type': ctx.obj['RC']['project_type']},
        output_dir=project_name)
