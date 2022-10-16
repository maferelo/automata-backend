#!/bin/bash

poetry install

poetry run pre-commit install --install-hooks

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

# Apply migrations
#alembic upgrade head
