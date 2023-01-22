#!/bin/bash

echo "source $(poetry env info --path)/bin/activate" >> ~/.bashrc

# Fix git dubious ownership error
git config --global --add safe.directory /app
# Fix git unable to undo changes
git config core.filemode false

alias run="gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --access-logfile - --reload"
