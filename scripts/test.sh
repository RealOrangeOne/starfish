#!/usr/bin/env bash

set -e

PATH=env/bin:${PATH}

set -x

black --check starfish/
flake8 starfish/
isort -c -rc starfish/
mypy starfish/
