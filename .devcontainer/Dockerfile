ARG VARIANT=3.8-bullseye

FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV \
        DEBIAN_FRONTEND=noninteractive \
        PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1

# Allow piped commands to fail at any step and run logging mode
SHELL ["/bin/bash", "-ceux", "-o", "pipefail"]

WORKDIR /app

COPY .devcontainer/postcreate.sh .devcontainer/

RUN \
        chmod +x .devcontainer/postcreate.sh; \
        chown -R vscode:vscode .devcontainer

USER vscode

RUN \
        mkdir -p \
        /home/vscode/.vscode-server/extensions \
        && chown -R vscode:vscode /home/vscode

RUN \
        --mount=type=cache,target=/home/vscode/.cache,uid=1000 \
        curl https://cli-assets.heroku.com/install.sh | sh; \
        curl -sSL https://install.python-poetry.org | python -

# Trigger build if files change
COPY \
        poetry.lock \
        pyproject.toml \
        .pre-commit-config.yaml \
        ./

COPY migrations .
