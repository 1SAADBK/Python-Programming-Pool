class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self._age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    print(rose.show())
    start_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        print(rose.show())
    growth = rose.height - start_height
    print(f"Growth this week: {round(growth, 1)}cm")
