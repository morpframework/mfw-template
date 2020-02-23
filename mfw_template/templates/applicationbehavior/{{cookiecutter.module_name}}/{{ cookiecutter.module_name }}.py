import typing
from dataclasses import dataclass, field
from morpcc.applicationbehavior.base import BaseBehavior

from ..app import App


class {{ cookiecutter.behavior_name }}Model(object):
    pass


class {{ cookiecutter.behavior_name }}ModelUI(object):
    pass


class {{ cookiecutter.behavior_name }}(BaseBehavior):
    model_marker = {{ cookiecutter.behavior_name }}Model
    modelui_marker = {{ cookiecutter.behavior_name }}ModelUI


@App.application_behavior("{{ cookiecutter.project_name }}.{{ cookiecutter.module_name }}")
def get_behavior(request):
    return {{ cookiecutter.behavior_name }}


