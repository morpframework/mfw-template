from ..app import App
from morpcc.behavior.base import BaseBehavior
from dataclasses import dataclass, field
import typing

@dataclass
class {{ cookiecutter.behavior_name }}Schema(object):
    pass

class {{ cookiecutter.behavior_name }}Model(object):
    pass

class {{ cookiecutter.behavior_name }}ModelUI(object):
    pass

class {{ cookiecutter.behavior_name }}Collection(object):
    pass

class {{ cookiecutter.behavior_name }}CollectionUI(object):
    pass

class {{ cookiecutter.behavior_name }}(BaseBehavior):

    schema = {{ cookiecutter.behavior_name }}Schema
    model_marker = {{ cookiecutter.behavior_name }}Model
    modelui_marker = {{ cookiecutter.behavior_name }}ModelUI
    collection_marker = {{ cookiecutter.behavior_name }}Collection
    collectionui_marker = {{ cookiecutter.behavior_name }}CollectionUI


@App.behavior('{{ cookiecutter.project_name }}.{{ cookiecutter.module_name }}')
def get_behavior(request):
    return {{ cookiecutter.behavior_name }}Behavior
