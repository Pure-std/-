import json
from typing import Any, Dict, List
from unittest.mock import Mock, mock_open, patch

from src.utils import read_json_data


def test_read_json_data_success() -> None:
    test_data: List[Dict[str, Any]] = [{"id": 1, "state": "EXECUTED"}]
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))) as mock_file:
        result = read_json_data("test.json")
        assert result == test_data
        mock_file.assert_called_once_with("test.json", "r", encoding="UTF-8")


@patch("builtins.open", side_effect=Exception("File not found"))
@patch("builtins.print")  # Правильный target для встроенной функции
def test_read_json_data_exception(mock_print: Mock, mock_open: Mock) -> None:
    result = read_json_data("invalid.json")
    assert result == []
    mock_print.assert_called_once_with("Exception at utils.py: File not found")
