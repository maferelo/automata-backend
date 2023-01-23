ARG IMAGE_VARIANT
ARG POETRY_VERSION

FROM mcr.microsoft.com/vscode/devcontainers/python:0-${IMAGE_VARIANT}

ARG POETRY_VERSION

ENV \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Allow piped commands to fail at any step and run, log command
SHELL ["/bin/bash", "-ceux", "-o", "pipefail"]

# Create cache directory to store all caches
RUN \
    mkdir -p ~/.cache

USER vscode

# Not working on M1
# RUN \
#     curl https://cli-assets.heroku.com/install.sh | sh;

RUN \
    mkdir -p \
    ~/.cache \
    /home/vscode/.vscode-server \
    ;

RUN \
    --mount=type=cache,target=/home/vscode/.cache,uid=1000 \
    curl -sSL https://install.python-poetry.org | \
        POETRY_VERSION=${POETRY_VERSION} python - \
        2>&1 | tee ~/install.poetry.log;

WORKDIR /app

COPY \
    poetry.lock \
    poetry.toml \
    pyproject.toml \
    ./

# Install Python dependencies
RUN \
    --mount=type=cache,target=/home/vscode/.cache/build.venv,uid=1000,gid=1000 \
    cp -nRT ~/.cache/build.venv .venv; \
    ~/.local/bin/poetry install \
        2>&1 | tee ~/install.poetry.dependencies.log; \
    cp -fnRT .venv ~/.cache/build.venv

COPY \
    .pre-commit-config.yaml \
    ./

# Install pre-commit hooks
RUN \
    --mount=type=cache,target=/home/vscode/.cache/build.pre-commit,uid=1000,gid=1000 \
    cp -nRT ~/.cache/build.pre-commit ~/.cache/pre-commit; \
    git init && ~/.local/bin/poetry run pre-commit install-hooks \
        2>&1 | tee ~/install.pre-commit.hooks.log; \
    cp -fnRT ~/.cache/pre-commit ~/.cache/build.pre-commit

COPY migrations .

# poetry run alembic upgrade head

COPY . .
