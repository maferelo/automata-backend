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
        apt-get update; \
        apt-get install -y --no-install-recommends python3-dev; \
        apt-get clean; \
        rm -rf /var/lib/apt/lists/*

RUN \
        chmod +x .devcontainer/postcreate.sh; \
        chown -R vscode:vscode .devcontainer

USER vscode

RUN \
        mkdir -p \
        /home/vscode/.vscode-server/extensions \
        /home/vscode/.cache/pre-commit; \
        chown -R vscode:vscode /home/vscode

RUN \
        --mount=type=cache,target=/home/vscode/.cache,uid=1000 \
        curl https://cli-assets.heroku.com/install.sh | sh; \
        curl https://pyenv.run | bash; \
        curl -sSL https://install.python-poetry.org | python -; \
        echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc

RUN \
        --mount=type=cache,target=/home/vscode/.cache,uid=1000 \
        export PATH="$HOME/.pyenv/bin:$PATH"; \
        pyenv install 3.9.15

# Trigger build if files change
COPY \
        .pre-commit-config.yaml \
        poetry.lock \
        poetry.toml \
        pyproject.toml \
        ./

COPY migrations .
