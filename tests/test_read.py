from unittest.mock import MagicMock, mock_open, patch

from src.read import read_csv, xlsx_read


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictReader")
def test_read_csv(mock_reader: MagicMock, mock_file: MagicMock) -> None:
    """Проверяет чтение CSV без привязки к путям"""
    # Arrange
    test_data = [{"id": 1}, {"id": 2}]
    mock_reader.return_value = test_data
    test_path = "data/test.csv"

    # Act
    result = read_csv(test_path)

    # Assert: проверяем только параметры открытия файла
    mock_file.assert_called_once_with(test_path, encoding="utf-8")
    mock_reader.assert_called_once_with(mock_file.return_value, delimiter=";")
    assert result == test_data


@patch("pandas.read_excel")
def test_xlsx_read(mock_read_excel: MagicMock) -> None:
    """Проверяет чтение Excel без привязки к путям"""
    # Arrange
    test_data = [{"id": 1}, {"id": 2}]
    mock_df = MagicMock()
    mock_df.to_dict.return_value = test_data
    mock_read_excel.return_value = mock_df
    test_path = "data/test.xlsx"

    # Act
    result = xlsx_read(test_path)

    # Assert: проверяем только факт вызова с нужным путем
    mock_read_excel.assert_called_once_with(test_path)
    mock_df.to_dict.assert_called_once_with("records")
    assert result == test_data
