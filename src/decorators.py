from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор для логирования вызовов функций."""

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> None:
            try:
                function(*args, **kwargs)
                result = f"{function.__name__} ok\n"
            except Exception as error:
                result = f"{function.__name__} error: {error}. Inputs: {args}, {kwargs}\n"
            if filename != "":
                with open(filename, "a", encoding="utf-8") as log_file:
                    log_file.write(result)
            else:
                print(result, end="")

        return inner

    return decorator
