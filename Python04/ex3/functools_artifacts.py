from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def sell_reducer(sells: list[int], operation: str) -> int:
    if not sells:
        return 0
    if operation == "add":
        return reduce(operator.add, sells)
    elif operation == "multiply":
        return reduce(operator.mul, sells)
    elif operation == "max":
        return reduce(lambda x, y: max([x, y]), sells)
    elif operation == "min":
        return reduce(lambda x, y: min([x, y]), sells)
    else:
        raise ValueError("Unknow Operator")


def partial_power(base_power: Callable) -> dict[str, Callable]:
    flame = partial(base_power, 50, "fire")
    pickaxe = partial(base_power, 50, "diamond")
    shovel = partial(base_power, 50, "rock")
    return {"flame": flame,
            "pickaxe": pickaxe,
            "shovel": shovel}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def sell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def sell_casting(sell) -> str:
        return "Unknown sell type"

    @sell_casting.register(int)
    def _int(sell: int) -> str:
        return f"Damage sell: {sell} damage"

    @sell_casting.register(str)
    def _str(sell: str) -> str:
        return f"power: {sell}"

    @sell_casting.register(list)
    def _list(sell: list) -> str:
        return f"Multi-cast: {len(sell)} sells"
    return sell_casting


if __name__ == "__main__":
    try:
        print("Testing spell reducer...")
        sells = [50, 30, 20]
        summe = sell_reducer(sells, "add")
        print(f"sum: {summe}")
        sells2 = [24, 10000]
        print(f"Product: {sell_reducer(sells2, "multiply")}")
        sells3 = [20, 40]
        print(f"Max: {sell_reducer(sells3, "max")}")
        print("\nTesting memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
        print("\nTesting sell dispatcher...")
        dispatcher = sell_dispatcher()
        print(dispatcher(1337))
        print(dispatcher("fire"))
        print(dispatcher(["sell1", "sell2", "sell3"]))
        print(dispatcher(4.3))
    except Exception as e:
        print(f"ERROR: {e}")
