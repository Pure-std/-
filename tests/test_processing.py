import pytest

from src.processing import filter_by_state, sort_by_date


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
