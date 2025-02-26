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
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == expected


def test_get_mask_card_number_with_fixture(card_number_data: list) -> None:
    for card_number, expected in card_number_data:
        result = get_mask_card_number(card_number)
        assert result == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [("1234567890", "**7890"), ("9876543210", "**3210"), ("1111222233", "**2233"), ("", "**"), ("1", "**1")],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)
    assert result == expected


def test_get_mask_account_with_fixture(account_number_data: list) -> None:
    for account_number, expected in account_number_data:
        result = get_mask_account(account_number)
        assert result == expected
