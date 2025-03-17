from typing import Any

from src.decorators import log


def test_successful_execution_console(capsys: Any) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    captured = capsys.readouterr()

    assert captured.out == "add ok\n"


def test_exception_handling_console(capsys: Any) -> None:
    @log()
    def raise_error() -> None:
        raise ValueError("Some error")

    raise_error()
    captured = capsys.readouterr()

    assert captured.out == "raise_error error: Some error. Inputs: (), {}\n"


def test_args_kwargs_logging(capsys: Any) -> None:
    @log()
    def func(a: Any, b: Any, c: Any = 3) -> None:
        raise RuntimeError("Oops")

    func(10, "arg", c=5)
    captured = capsys.readouterr()
    expected_output = "func error: Oops. Inputs: (10, 'arg'), {'c': 5}\n"

    assert captured.out == expected_output


def test_success_log_to_file(tmp_path: Any) -> None:
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def test_func() -> None:
        pass

    test_func()
    content = filename.read_text(encoding="utf-8")

    assert content == "test_func ok\n"


def test_error_log_to_file(tmp_path: Any) -> None:
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def test_func() -> None:
        raise TypeError("Bad type")

    test_func()
    content = filename.read_text(encoding="utf-8")

    assert content == "test_func error: Bad type. Inputs: (), {}\n"


def test_multiple_calls_append(tmp_path: Any) -> None:
    filename = tmp_path / "test.log"

    @log(filename=str(filename))
    def test_func() -> None:
        pass

    test_func()
    test_func()
    content = filename.read_text(encoding="utf-8")

    assert content == "test_func ok\ntest_func ok\n"


def test_no_file_created(tmp_path: Any) -> None:
    @log()
    def func() -> None:
        pass

    func()

    assert len(list(tmp_path.iterdir())) == 0


def test_various_arguments(capsys: Any) -> None:
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    divide(4, 2)
    captured = capsys.readouterr()

    assert captured.out == "divide ok\n"

    divide(1, 0)
    captured = capsys.readouterr()

    assert "divide error: division by zero. Inputs: (1, 0), {}" in captured.out
