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


@pytest.fixture
def sample_transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264136,
            "state": "EXECUTED",
            "date": "2019-04-04T23:21:06.223318",
            "operationAmount": {"amount": "231.0", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264136,
            "state": "EXECUTED",
            "date": "2019-04-04T23:21:99.233458",
            "operationAmount": {"amount": "21123.0", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264136,
            "state": "EXECUTED",
            "date": "2019-04-04T23:22:12.121331",
            "operationAmount": {"amount": "2356.0", "currency": {"name": "JPY", "code": "JPY"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
