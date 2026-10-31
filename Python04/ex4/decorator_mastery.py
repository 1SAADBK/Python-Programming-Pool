from functools import wraps
from collections.abc import Callable
from time import time, sleep
from typing import Any


def sell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time() - start
        print(f"Sell completed in {round(end, 3)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def updated_function(*args: Any, **kwargs: Any) -> Any:
            power_value = kwargs.get("power")
            if isinstance(power_value, int) and power_value >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this sell"
        return updated_function
    return decorator


def retry_sell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def retry_to_max(*args: Any, **kwargs: Any) -> Any:
            for n in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Sell failed, retrying... "
                          f"(attempts {n + 1}/{max_attempts})")
            return f"Sell casting failed after {max_attempts} attempts"
        return retry_to_max
    return decorator


class MazeGuild():
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def validate_maze_name(name: str) -> bool:
        if (len(name) > 2
                and all(char.isalpha() or char.isspace() for char in name)):
            return True
        return False

    @power_validator(10)
    def cast_sell(self, sell_name: str, power: int) -> str:
        return f"Successfully cast {sell_name} with <{power}> power"


if __name__ == "__main__":
    print("Testing sell timer...")

    @sell_timer
    def sell() -> str:
        sleep(0.1)
        return "Sell casted!"
    s = sell()
    print(f"result: {s}")
    print("\nTesting retrying sell...")

    @retry_sell(3)
    def sell2() -> float:
        n = 3000/0
        return n
    sell2()
    print("Waaagh didn't work")
    print("\nTesting MazeGuide !")
    valid_mg_name = MazeGuild("amazing")
    print(valid_mg_name.validate_maze_name(valid_mg_name.name))
    not_valid_mg_name = MazeGuild("a-maze-ing")
    print(not_valid_mg_name.validate_maze_name(not_valid_mg_name.name))
    print(valid_mg_name.cast_sell("sell", power=15))
    print(valid_mg_name.cast_sell("sell", power=3))
