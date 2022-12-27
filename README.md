# Automata

> Personal scripts for automation of everyday tasks
> using best practices with reference notes.

[![codecov](https://codecov.io/gh/maferelo/automata-backend/branch/develop/graph/badge.svg?token=GWW6DXXDZO)](https://codecov.io/gh/maferelo/automata-backend)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/maferelo/automata-backend/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/maferelo/automata-backend/tree/main)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Prerequisites

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata
```

### For Mac

- [Docker](https://www.docker.com/)
- [Homebrew](https://brew.sh/)

```bash
bash scripts/prestart-mac.sh
```

## Development

We use [remote containers](https://code.visualstudio.com/docs/remote/containers-tutorial).

1. Press F1 to open the Command Palette.
2. Type reopen in container.
3. Select Remote Containers: Reopen in Container from the list of available options.

Inside the container run:

```bash
poetry run app
```

Check the endpoint

```bash
curl --location --request GET 'http://localhost:8000/'
```

### Linting

```bash
pre-commit run --all-files
```

### Dependencies

Use the package manager [poetry](https://python-poetry.org/) to install requirements

```bash
poetry add darglint --group dev
```

### Database migrations

Using [Alembic](https://alembic.sqlalchemy.org/en/latest/)

Change models and commit

```bash
alembic revision --autogenerate -m "<message>"
alembic upgrade head
```

### Tests

```bash
nox --session tests -- tests/test_console.py
```

End to end testing

```bash
nox -s tests -- -m e2e
```

## Deployments

Using [Heroku](https://python-poetry.org/) Create staging and production apps

```bash
heroku apps create automata-backend
heroku stack:set -a automata-backend heroku-20
heroku buildpacks:add -a automata-backend \
  https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add -a automata-backend heroku/python
heroku config:set POETRY_VERSION=1.3.1
```

```bash
heroku login
git push heroku main
heroku open
heroku logs --tail
```

## References

- [Project homepage](https://your.github.com/automata/)
- [Repository](https://github.com/maferelo/automata/)
- [Issue tracker](https://github.com/your/maferelo/issues)
  - In case of sensitive bugs like security vulnerabilities, please contact
    maferelo13@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects
  - Your other project
  - Someone else's project
  - [Awesome README](https://github.com/matiassingers/awesome*readme)
