import subprocess

from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email
