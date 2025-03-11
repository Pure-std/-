import pytest

from src.generators import card_number_generator, filters_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [939719570, 142264268]),
        ("EUR", [142264136, 142264136]),
        ("", []),
    ],
)
def test_filters_by_currency(sample_transactions: list, currency: str, expected_ids: int) -> None:
    result = list(filters_by_currency(sample_transactions, currency))
    assert [t["id"] for t in result] == expected_ids


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [{"description": "Payment"}, {"description": "Transfer"}, {"description": "Withdrawal"}],
            ["Payment", "Transfer", "Withdrawal"],
        ),
        ([{"id": 1}, {"description": "Test"}, {}], [None, "Test", None]),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions: list, expected: str) -> None:
    assert list(transaction_descriptions(transactions)) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (0, 0, ["0000 0000 0000 0000"]),
        (123456, 123456, ["0000 0000 0012 3456"]),
        (10, 5, []),
    ],
)
def test_card_number_generator(start: int, end: int, expected: str) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected
