#!/bin/bash

poetry install

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

git config --global --add safe.directory /app

poetry run pre-commit install --install-hooks

#poetry run alembic upgrade head

#poetry run pre-commit run -a
