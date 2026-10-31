class Plant:
    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name = name.capitalize()
        if height >= 0:
            self._height = float(height)
        else:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        if age >= 0:
            self._age = int(age)
        else:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
        self._growth_rate = growth_rate

    def age(self, days: int) -> None:
        self._age += days

    def grow(self, days: int) -> None:
        self._height += self._growth_rate * days

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}:  Error, height can't"
                  f" be negative\nHeight update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't"
                  f" be negative\nAge update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        return f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"


class Flower(Plant):
    def __init__(
        self, name: str, height: float,
        age: int, growth_rate: float, color: str
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self) -> None:
        print(super().show())
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        growth_rate: float, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              f" {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        print(super().show())
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        growth_rate: float, harvest_season: str, nutritional_value: int
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, days: int) -> None:
        super().grow(days)

    def show(self) -> None:
        print(super().show())
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15.0, 10, 1, "red")
    oak = Tree("oak", 200.0, 365, 0.5, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, 2.1, "April", 0)
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show()
