#!/bin/bash

poetry install

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

#poetry run alembic upgrade head

git init .

poetry run pre-commit install --install-hooks

#poetry run pre-commit run -a
