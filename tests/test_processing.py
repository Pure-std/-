import pytest

from src.processing import count_operations_by_category, filter_by_description, filter_by_state, sort_by_date


def test_filter_by_state_default(sample_operations: list) -> None:
    filtered = filter_by_state(sample_operations)
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)


def test_filter_by_state_canceled(sample_operations: list) -> None:
    filtered = filter_by_state(sample_operations, "CANCELED")
    assert len(filtered) == 1
    assert filtered[0]["state"] == "CANCELED"


def test_sort_by_date_default(sample_operations: list) -> None:
    sorted_ops = sort_by_date(sample_operations)
    expected_dates = ["2023-01-01", "2022-01-01", "2021-01-01", "2020-01-01"]
    assert [op["date"] for op in sorted_ops] == expected_dates


def test_sort_by_date_ascending(sample_operations: list) -> None:
    sorted_ops = sort_by_date(sample_operations, reverse_parameter=False)
    expected_dates = ["2020-01-01", "2021-01-01", "2022-01-01", "2023-01-01"]
    assert [op["date"] for op in sorted_ops] == expected_dates


test_data_filter = [
    ([], "EXECUTED", []),
    ([{"state": "EXECUTED"}], "EXECUTED", [{"state": "EXECUTED"}]),
    ([{"state": "CANCELED"}], "EXECUTED", []),
    (
        [{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "EXECUTED"}],
        "EXECUTED",
        [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
    ),
    ([{"state": "executed"}], "EXECUTED", []),
    (
        [{"state": "EXECUTED"}, {"state": "EXECUTED", "date": "2024-01-01"}],
        "EXECUTED",
        [{"state": "EXECUTED"}, {"state": "EXECUTED", "date": "2024-01-01"}],
    ),
]


@pytest.mark.parametrize("operations, state, expected", test_data_filter)
def test_filter_by_state_parametrized(operations: list, state: str, expected: str) -> None:
    result = filter_by_state(operations, state)
    assert result == expected


test_data_sort = [
    (
        [{"date": "2023-01-01"}, {"date": "2022-01-01"}],
        True,
        [{"date": "2023-01-01"}, {"date": "2022-01-01"}],
    ),
    (
        [{"date": "2022-01-01"}, {"date": "2023-01-01"}],
        True,
        [{"date": "2023-01-01"}, {"date": "2022-01-01"}],
    ),
    (
        [{"date": "2022-01-01"}, {"date": "2023-01-01"}],
        False,
        [{"date": "2022-01-01"}, {"date": "2023-01-01"}],
    ),
    ([], True, []),
    ([{"date": "2023-01-01"}], True, [{"date": "2023-01-01"}]),
    (
        [{"date": "2023-01-01"}, {"date": "2023-01-01"}],
        True,
        [{"date": "2023-01-01"}, {"date": "2023-01-01"}],
    ),
    (
        [{"date": "2021-01-01"}, {"date": "2020-01-01"}, {"date": "2023-01-01"}],
        False,
        [{"date": "2020-01-01"}, {"date": "2021-01-01"}, {"date": "2023-01-01"}],
    ),
]


@pytest.mark.parametrize("operations, reverse_parameter, expected", test_data_sort)
def test_sort_by_date_parametrized(operations: list, reverse_parameter: bool, expected: str) -> None:
    sorted_ops = sort_by_date(operations, reverse_parameter)
    assert sorted_ops == expected


@pytest.mark.parametrize(
    "operations, categories, expected",
    [
        # Базовый тест
        (
            [{"description": "A"}, {"description": "A"}, {"description": "B"}, {"description": "C"}],
            ["A", "B", "D"],
            {"A": 2, "B": 1, "D": 0},
        ),
        # Пустые операции
        ([], ["A", "B"], {"A": 0, "B": 0}),
        # Пустые категории
        ([{"description": "A"}], [], {}),
        # Нет совпадений
        ([{"description": "C"}, {"description": "D"}], ["A", "B"], {"A": 0, "B": 0}),
        # Все категории существуют
        ([{"description": "A"}, {"description": "B"}], ["A", "B"], {"A": 1, "B": 1}),
        # Операции без описания (покрываем условие op.get('description'))
        ([{"id": 1}, {"description": None}, {"description": "A"}], ["A"], {"A": 1}),
    ],
)
def test_count_operations_by_category(operations: list, categories: list, expected: str) -> None:
    assert count_operations_by_category(operations, categories) == expected


@pytest.mark.parametrize(
    "operations, pattern, expected",
    [
        # Базовые совпадения
        ([{"description": "Payment"}, {"description": "Transfer"}], "Transfer", [{"description": "Transfer"}]),
        # Регулярные выражения
        ([{"description": "Invoice 123"}, {"description": "Receipt 45X"}], r"\d{3}", [{"description": "Invoice 123"}]),
        # Нет совпадений
        ([{"description": "Deposit"}, {"description": "Withdrawal"}], "Credit", []),
        # Пустые данные
        ([], "any", []),
        # Регистрозависимость
        ([{"description": "Apple"}, {"description": "apple"}], "Apple", [{"description": "Apple"}]),
        # Спецсимволы в паттерне
        ([{"description": "file.txt"}, {"description": "data"}], r"\.txt", [{"description": "file.txt"}]),
        # Пустой паттерн (совпадает с любым описанием)
        ([{"description": "Test"}, {"description": ""}], "", [{"description": "Test"}, {"description": ""}]),
        # Частичное совпадение
        ([{"description": "Monthly payment"}, {"description": "Bonus"}], "pay", [{"description": "Monthly payment"}]),
    ],
)
def test_filter_by_description(operations: list, pattern: str, expected: str) -> None:
    result = filter_by_description(operations, pattern)
    assert result == expected


# Тест на обработку ошибок (если требуется)
def test_key_error_for_missing_description() -> None:
    with pytest.raises(KeyError):
        filter_by_description([{"id": 1}], "any")
