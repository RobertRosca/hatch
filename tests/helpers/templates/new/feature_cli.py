from hatch.template import File
from hatch.utils.fs import Path

from ..licenses import MIT


def get_files(**kwargs):
    return [
        File(
            Path('LICENSE.txt'),
            MIT.replace('<year>', f"{kwargs['year']}-present", 1).replace(
                '<copyright holders>', f"{kwargs['author']} <{kwargs['email']}>", 1
            ),
        ),
        File(
            Path('src', kwargs['package_name'], '__init__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
""",
        ),
        File(
            Path('src', kwargs['package_name'], '__about__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
__version__ = '0.0.1'
""",
        ),
        File(
            Path('src', kwargs['package_name'], '__main__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == '__main__':
    from .cli import {kwargs['package_name']}

    sys.exit({kwargs['package_name']}())
""",
        ),
        File(
            Path('src', kwargs['package_name'], 'cli', '__init__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
import click

from ..__about__ import __version__


@click.group(context_settings={{'help_option_names': ['-h', '--help']}}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name={kwargs['project_name']!r})
@click.pass_context
def {kwargs['package_name']}(ctx: click.Context):
    click.echo('Hello world!')
""",
        ),
        File(
            Path('tests', '__init__.py'),
            f"""\
# SPDX-FileCopyrightText: {kwargs['year']}-present {kwargs['author']} <{kwargs['email']}>
#
# SPDX-License-Identifier: MIT
""",
        ),
        File(
            Path('README.md'),
            f"""\
# {kwargs['project_name']}

[![PyPI - Version](https://img.shields.io/pypi/v/{kwargs['project_name_normalized']}.svg)](https://pypi.org/project/{kwargs['project_name_normalized']})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{kwargs['project_name_normalized']}.svg)](https://pypi.org/project/{kwargs['project_name_normalized']})

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install {kwargs['project_name_normalized']}
```

## License

`{kwargs['project_name_normalized']}` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
""",  # noqa: E501
        ),
        File(
            Path('pyproject.toml'),
            f"""\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{kwargs['project_name_normalized']}"
description = ''
readme = "README.md"
requires-python = ">=3.7"
license = "MIT"
keywords = []
authors = [
  {{ name = "{kwargs['author']}", email = "{kwargs['email']}" }},
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dependencies = [
  "click",
]
dynamic = ["version"]

[project.urls]
Documentation = "https://github.com/unknown/{kwargs['project_name_normalized']}#readme"
Issues = "https://github.com/unknown/{kwargs['project_name_normalized']}/issues"
Source = "https://github.com/unknown/{kwargs['project_name_normalized']}"

[project.scripts]
{kwargs['project_name_normalized']} = "{kwargs['package_name']}.cli:{kwargs['package_name']}"

[tool.hatch.version]
path = "src/{kwargs['package_name']}/__about__.py"

[tool.hatch.envs.default]
dependencies = [
  "pytest",
  "pytest-cov",
]
[tool.hatch.envs.default.scripts]
cov = "pytest --cov-report=term-missing --cov-config=pyproject.toml --cov=src/{kwargs['package_name']} --cov=tests {{args}}"
no-cov = "cov --no-cov {{args}}"

[[tool.hatch.envs.test.matrix]]
python = ["3.7", "3.8", "3.9", "3.10", "3.11"]

[tool.coverage.run]
branch = true
parallel = true
omit = [
  "src/{kwargs['package_name']}/__about__.py",
]

[tool.coverage.report]
exclude_lines = [
  "no cov",
  "if __name__ == .__main__.:",
  "if TYPE_CHECKING:",
]
""",  # noqa: E501
        ),
    ]
