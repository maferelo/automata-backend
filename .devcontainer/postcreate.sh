#!/bin/bash

poetry install

git init .

poetry run pre-commit install --install-hooks

poetry run pre-commit run -a

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

# Apply migrations
#alembic upgrade head
