"""A module to set recurrent tasks using cronjobs."""
from pathlib import Path

from automata.config import paths
from automata.config import scheluder_scripts
from automata.logger import logger
from automata.utils import log_start_and_finish_decorator
from crontab import CronTab


def add_logging_and_timestamps_to_command(script_file_path: Path, name: str) -> str:
    """Add start and finish timestamp logs to a bash script."""
    timestamp_command = ";".join(
        (
            f"{paths.python_executable} {paths.main} log-message start-{name}",
            f"sh {script_file_path}",
            f"{paths.python_executable} {paths.main} log-message end-{name}",
        )
    )
    return f"({timestamp_command}) >> {paths.log_file} 2>&1"  # output to log file


def create_command(name: str) -> str:
    """Create a command to run and log the script in bash if exists."""
    script_file_path = paths.scripts / f"{name}.sh"
    if script_file_path.exists() is False:
        logger.error("Script file %s does not exist.", script_file_path)
        return ""
    return add_logging_and_timestamps_to_command(script_file_path, name)


def set_job(day: int, name: str, crontab_session: CronTab) -> None:
    """Set a cronjob for an arbitrary day at 00:00 a.m."""
    command = create_command(name)
    if command == "":
        return
    helper_text = f"Logging start and end for {name} execution."
    cron_job = crontab_session.new(command=command, comment=helper_text)
    cron_job.setall(f"0 0 {day} * *")


@log_start_and_finish_decorator(logger)
def reset_jobs() -> None:
    """Reset the cronjobs to run daily from start of month."""
    with CronTab(user="root") as crontab_session:
        crontab_session.remove_all()
        for day, name in enumerate(scheluder_scripts, start=1):
            set_job(day, name, crontab_session)
