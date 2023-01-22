ARG IMAGE=tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim


FROM ${IMAGE} as stage

WORKDIR /tmp

ENV DEBIAN_FRONTEND noninteractive

# Allow piped commands to fail at any step
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./

RUN \
    export PATH="/root/.local/bin:$PATH" \
    && poetry export \
        -f requirements.txt \
        --output requirements.txt \
        --without-hashes \
        --only main

FROM ${IMAGE}

RUN addgroup --system app && adduser --system --group app

USER app

WORKDIR /app

COPY --from=stage /tmp/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

ENV PATH=${PATH}:/home/app/.local/bin \
    PYTHONPATH=${PYTHONPATH}:/home/app/.local/lib/python3.8/site-packages \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=

COPY . .
