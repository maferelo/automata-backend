"""Nox sessions."""
from pathlib import Path

import nox
from nox_poetry import Session
from nox_poetry import session as _session

PYTHON_VERSION = "3.8"

LOCATIONS = ["src", "tests", "noxfile.py", "docs/conf.py"]
nox.options.sessions = (
    "docs",
    "tests",
    "typeguard",
)


@_session(python=PYTHON_VERSION, reuse_venv=True)
def coverage(session: Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report"]

    session.install("coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


@nox.session(python=False)
def docs(session: Session) -> None:
    """Build the documentation."""
    session.run("sphinx-build", "docs", "docs/_build")


@_session(python=PYTHON_VERSION, reuse_venv=True)
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    requirements = session.poetry.export_requirements()
    session.install("safety")
    session.run("safety", "check", "--full-report", f"--file={requirements}")


@_session(python=PYTHON_VERSION, reuse_venv=True)
def tests(session: Session) -> None:
    """Run the test suite."""
    session.install(".")
    session.install("coverage", "pytest", "pytest-mock", "pygments")
    try:
        session.run("coverage", "run", "--parallel", "-m", "pytest", *session.posargs)
    finally:
        if session.interactive:
            session.notify("coverage", posargs=[])


@_session(python=PYTHON_VERSION, reuse_venv=True)
def typeguard(session: Session) -> None:
    """Runtime type checking using Typeguard."""
    session.install(".")
    session.install("pytest", "typeguard", "pytest-mock", "pygments")
    session.run("pytest", "--typeguard-packages=app", *session.posargs)
