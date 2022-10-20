#!/bin/bash

poetry install

git init .

poetry run pre-commit install --install-hooks

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

poetry run nox -r

# Apply migrations
#alembic upgrade head
