from collections.abc import Callable


def maze_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def sell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def add_power(to_add: int) -> int:
        nonlocal power
        power += to_add
        return power
    return add_power


def power_factory(power_type: str) -> Callable:
    def applies_power(item_name: str) -> str:
        return f"{power_type} {item_name}"
    return applies_power


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {'store': store,
            'recall': recall}


if __name__ == "__main__":
    print("Testing maze counter...")
    counter_a = maze_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = maze_counter()
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting sell accumulator...")
    add_power = sell_accumulator(100)
    print(f"Base 100, add 20: {add_power(20)}")
    print(f"Base 100, add 30: {add_power(30)}")
    print("\nTesting power factory...")
    flaming_power = power_factory("Flaming")
    frozen_power = power_factory("Frozen")
    print(flaming_power("Sword"))
    print(frozen_power("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 1337")
    vault['store']('secret', 1337)
    print(f"Recall 'secret': {vault['recall']('secret')}")
