from collections.abc import Callable


def sell_combiner(sell1: Callable, sell2: Callable) -> Callable:
    def call_two(target: str, power: int) -> tuple[str, str]:
        sell1_str = sell1(target, power)
        sell2_str = sell2(target, power)
        return (sell1_str, sell2_str)
    return call_two


def power_amplifier(base_sell: Callable, multiplier: int) -> Callable:
    def multiplied(target: str, power: int) -> str:
        string = base_sell(target, power * multiplier)
        return string
    return multiplied


def conditional_caster(condition: Callable, sell: Callable) -> Callable:
    def caster(target: str, power: int) -> Callable | str:
        if condition(target, power):
            return sell(target, power)
        return "sell canceled"
    return caster


def sell_sequence(sells: list[Callable]) -> Callable:
    def cast_all_sells(target: str, power: int) -> list[str]:
        results = []
        for sell in sells:
            results.append(sell(target, power))
        return results
    return cast_all_sells


def medicine(target: str, power: int) -> str:
    return f"the medicine heals {target} for {power}HP"


def food(target: str, power: int) -> str:
    return f"{target} got {power} power from eating food"


if __name__ == "__main__":
    print("\nTesting sell combiner...")
    combiner = sell_combiner(medicine, food)
    print(f"Combined sell result: {combiner("player", 15)[0]},"
          f" {combiner("player", 15)[1]}")
    print("\nTesting power amplifier...")
    amplifier = power_amplifier(medicine, 2)
    print(f"Original: {medicine("player", 15)}, "
          f"Amplified: {amplifier("Player", 15)}")
