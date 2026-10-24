"""Input validation for potentially billable outbound call destinations."""

import re

_E164_PATTERN = re.compile(r"\+[1-9]\d{7,14}\Z")


def require_e164_phone_number(value: str | None) -> str:
    """Return a normalized E.164 number or fail before the call is placed."""
    if not isinstance(value, str):
        raise ValueError("Job metadata must contain one E.164 phone number")
    number = value.strip()
    if not _E164_PATTERN.fullmatch(number):
        raise ValueError("Outbound destination must be a valid E.164 phone number")
    return number
