from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.read import read_csv, xlsx_read


@patch("builtins.open", new_callable=mock_open)
@patch("src.read.csv.DictReader")
@patch("src.read.Path.cwd")
def test_read_csv(
    mock_cwd: MagicMock,
    mock_dict_reader: MagicMock,
    mock_file: MagicMock,
) -> None:
    """Тестирование чтения CSV с проверкой пути и параметров"""
    # Мокируем текущий каталог
    mock_cwd.return_value = Path("/fake/dir")

    # Ожидаемые данные и путь
    test_data = [{"amount": "100"}, {"amount": "200"}]
    expected_path = Path("/fake/dir").parent / "data/transactions.csv"

    # Настраиваем поведение DictReader
    mock_dict_reader.return_value = test_data

    # Вызываем тестируемую функцию
    result = read_csv("data/transactions.csv")

    # Проверяем вызовы
    mock_file.assert_called_once_with(expected_path, encoding="utf-8")
    mock_dict_reader.assert_called_once_with(mock_file.return_value, delimiter=";")
    assert result == test_data


@patch("src.read.pd.read_excel")
@patch("src.read.Path.cwd")
def test_xlsx_read(
    mock_cwd: MagicMock,
    mock_read_excel: MagicMock,
) -> None:
    """Тестирование чтения Excel с проверкой конвертации"""
    # Мокируем текущий каталог
    mock_cwd.return_value = Path("/fake/dir")

    # Ожидаемые данные и путь
    test_data = [{"id": 1}, {"id": 2}]
    expected_path = Path("/fake/dir").parent / "data/transactions_excel.xlsx"

    # Мокируем DataFrame
    mock_df = MagicMock(spec=pd.DataFrame)
    mock_df.to_dict.return_value = test_data
    mock_read_excel.return_value = mock_df

    # Вызываем тестируемую функцию
    result = xlsx_read("data/transactions_excel.xlsx")

    # Проверяем вызовы
    mock_read_excel.assert_called_once_with(expected_path)
    mock_df.to_dict.assert_called_once_with("records")
    assert result == test_data
