import subprocess

from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    """
    Retrieve the Git user's name.

    Args:
        default (str): Default value if the Git user's name is not configured.

    Returns:
        str: The Git user's name.
    """
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    """
    Retrieve the Git user's email.

    Args:
        default (str): Default value if the Git user's email is not configured.

    Returns:
        str: The Git user's email.
    """
    return subprocess.getoutput("git config user.email").strip() or default


class GitExtension(Extension):
    """Jinja2 extension to provide filters for retrieving Git user information."""

    def __init__(self, environment):
        """
        Initialize the extension.

        Args:
            environment: The Jinja2 environment.
        """
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email
