from datetime import date

from jinja2.ext import Extension


class CurrentYearExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year
