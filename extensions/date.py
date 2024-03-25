from datetime import datetime, timedelta, timezone

from jinja2.ext import Extension


class CurrentYearExtension(Extension):
    """Jinja2 extension to provide current year as a global variable in templates."""

    def __init__(self, environment):
        """
        Initialize the extension.

        Args:
            environment: The Jinja2 environment.
        """
        super().__init__(environment)
        timezone_offset = +1.0  # CET (UTC+01:00)
        tzinfo = timezone(timedelta(hours=timezone_offset))
        environment.globals["current_year"] = datetime.now(tzinfo).year
