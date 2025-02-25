import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
        ("2020-02-29T15:30:00.000000", "29.02.2020"),
    ],
)
def test_get_date_parametrized(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


def test_get_date_fixture(date_data: list) -> None:
    for date_str, formatted_date in date_data:
        assert get_date(date_str) == formatted_date


def test_mask_account_card_fixtures(card_samples: list) -> None:
    for input_str, expected in card_samples:
        assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
        ("Карта 12345", "Карта 1234 5"),
        ("Amex ", "Amex"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 0000", "Счёт **0000"),
        ("Счет 1", "Счет **1"),
        ("Счет ", "Счет"),
    ],
)
def test_mask_account_card_parametrized(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected
