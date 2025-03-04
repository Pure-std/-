import pytest


@pytest.fixture
def card_number_data() -> list:
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("", ""),
        ("123", "123"),
    ]


@pytest.fixture
def account_number_data() -> list:
    return [("1234567890", "**7890"), ("9876543210", "**3210"), ("1111222233", "**2233"), ("", "**"), ("1", "**1")]


@pytest.fixture
def date_data() -> list:
    return [("2024-03-11T02:26:18.671407", "11.03.2024"), ("1999-12-31T23:59:59.999999", "31.12.1999")]


@pytest.fixture
def card_samples() -> list:
    return [
        ("Maestro 9876543210987654", "Maestro 9876 54** **** 7654"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa Classic 0000000000000000", "Visa Classic 0000 00** **** 0000"),
        ("", ""),
        ("Счет ", "Счет"),
        ("Карта", "Карта"),
    ]


@pytest.fixture
def sample_operations() -> list:
    return [
        {"state": "EXECUTED", "date": "2022-01-01"},
        {"state": "CANCELED", "date": "2023-01-01"},
        {"state": "EXECUTED", "date": "2021-01-01"},
        {"state": "PENDING", "date": "2020-01-01"},
    ]
