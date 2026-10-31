def print_plant_info(name: str, height: int, age: int) -> None:
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    name = "Rose"
    height = 25
    age = 30
    print_plant_info(name, height, age)
    print("\n=== End of Program ===")
