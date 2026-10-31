def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp >= 0 and temp <= 40:
        return temp
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0)")
    else:
        raise ValueError(f"{temp}°C is too hot for plants (max 40)")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    data = ["25", "abc", "100", "-50"]
    for string in data:
        try:
            print(f"\nInput data is '{string}'")
            temp = input_temperature(string)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
