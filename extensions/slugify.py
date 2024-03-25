import re
import unicodedata

from jinja2.ext import Extension


def slugify(value, separator="-"):
    value = (
        unicodedata.normalize("NFKD", str(value))
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify
