class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self):
        return f"{self.name}: {round(self.height, 1)}cm, {self._age} days old"


if __name__ == "__main__":
    plants_raw_data = [
        ("Rose", 25.0, 30, 1),
        ("Oak", 200.0, 365, 2),
        ("Cactus", 5.0, 90, 1),
        ("Sunflower", 80.0, 45, 2),
        ("Fern", 15.0, 120, 1)
    ]
    garden = []
    print("=== Plant Factory Output ===")
    for name, height, age, growth_rate in plants_raw_data:
        new_plant = Plant(name, height, age, growth_rate)
        garden.append(new_plant)
        print(f"Created: {new_plant.show()}")
