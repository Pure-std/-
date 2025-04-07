from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", ""),
        ("123", "123"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_input, expected",
    [
        (1234567890123456, ""),
        (None, ""),
        (1234, ""),
        ({"key": "value"}, ""),
    ],
)
def test_get_mask_card_number_invalid(invalid_input: Any, expected: str) -> None:
    result = get_mask_card_number(invalid_input)
    assert result == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),
        ("9876543210", "**3210"),
        ("1111222233", "**2233"),
        ("", "**"),
        ("1", "**1"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_input, expected",
    [
        (1234567890, ""),
        (None, ""),
        (5678, ""),
        ({"key": "value"}, ""),
    ],
)
def test_get_mask_account_invalid(invalid_input: Any, expected: str) -> None:
    result = get_mask_account(invalid_input)
    assert result == expected
