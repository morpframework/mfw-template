import morpfw
from dataclasses import dataclass, field
import typing


@dataclass
class {{ cookiecutter.type_name }}Schema(morpfw.Schema):

    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
