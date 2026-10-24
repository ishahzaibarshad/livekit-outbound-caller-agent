import pytest

from safety import require_e164_phone_number


def test_e164_destination_is_trimmed_and_returned():
    assert require_e164_phone_number("  +12025550100  ") == "+12025550100"


@pytest.mark.parametrize("value", [None, "", "2025550100", "+1", "sip:user@example.com"])
def test_invalid_destination_is_rejected_before_call_placement(value):
    with pytest.raises(ValueError, match="E.164"):
        require_e164_phone_number(value)
