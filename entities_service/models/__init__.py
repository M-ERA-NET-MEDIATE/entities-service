"""SOFT models."""

from __future__ import annotations

import re

URI_REGEX = re.compile(r"^(?P<namespace>https?://.+)/(?P<version>\d(?:\.\d+){0,2})/(?P<name>[^/#?]+)$")
"""Regular expression to parse a SOFT entity URI."""

__all__ = ("URI_REGEX",)
