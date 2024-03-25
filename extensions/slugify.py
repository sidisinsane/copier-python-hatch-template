import re
import unicodedata

from jinja2.ext import Extension


def slugify(value, separator="-"):
    """
    Convert a string to a slug.

    Args:
        value (str): The string to slugify.
        separator (str, optional): The separator to use between words. Defaults to "-".

    Returns:
        str: The slugified string.
    """
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class SlugifyExtension(Extension):
    """Jinja2 extension to provide a filter for converting strings to slugs."""

    def __init__(self, environment):
        """
        Initialize the extension.

        Args:
            environment: The Jinja2 environment.
        """
        super().__init__(environment)
        environment.filters["slugify"] = slugify
