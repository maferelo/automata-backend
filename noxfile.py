"""Nox sessions."""
import nox

MODULE_PATH = "src/"
nox.options.sessions = (
    "docs",
    "mypy",
    "tests",
    "typeguard",
    "safety",
    "xdoctest",
    "coverage",
)


@nox.session(python=False)
def coverage(session: nox.Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["html"]
    session.run("coverage", *args)


@nox.session(python=False)
def mypy(session: nox.Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["."]
    session.run("mypy", *args)


@nox.session(python=False)
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    session.run("sphinx-build", "docs", "docs/_build", "-W")


@nox.session(python=False)
def safety(session: nox.Session) -> None:
    """Scan dependencies for insecure packages."""
    args = session.posargs or []
    session.run("safety", "check", "--full-report", "--file=poetry.lock", *args)


@nox.session(python=False)
def tests(session: nox.Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["-m", "not e2e"]
    session.run(
        "pytest",
        "-n",
        "4",
        "--cov",
        "src",
        "--junitxml=test-results/junit.xml",
        *args,
    )


@nox.session(python=False)
def typeguard(session: nox.Session) -> None:
    """Runtime type checking using Typeguard."""
    args = session.posargs or ["-m", "not e2e"]
    session.run(
        "pytest",
        "--typeguard-packages=src",
        "-n",
        "4",
        "--junitxml=test-results/junit.xml",
        *args,
    )


@nox.session(python=False)
def xdoctest(session: nox.Session) -> None:
    """Run examples with xdoctest."""
    args = session.posargs or ["all"]
    session.run("python", "-m", "xdoctest", MODULE_PATH, *args)
