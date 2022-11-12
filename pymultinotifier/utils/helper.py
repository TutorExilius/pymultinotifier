"""Helper functions"""

import re


def camel_to_snake_case(value: str) -> str:
    """Convert string to camel case string."""

    return re.sub(r"(?<=[a-z])()(?=[A-Z])|(?<!^)()(?=[A-Z][a-z])", "_", value).lower()
