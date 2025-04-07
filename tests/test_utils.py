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
@patch("src.utils.logger.error")
def test_read_json_data_exception(mock_logger_error: Mock, mock_open: Mock) -> None:
    result = read_json_data("invalid.json")
    assert result == []
    mock_logger_error.assert_called_once_with("read_json_data: File not found")
