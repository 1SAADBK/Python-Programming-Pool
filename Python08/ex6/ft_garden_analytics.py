class Plant:
    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 1)

    class Stats:
        def __init__(self) -> None:
            self._grow_times = 0
            self._age_times = 0
            self._show_times = 0

        def grow_record(self) -> None:
            self._grow_times += 1

        def age_record(self) -> None:
            self._age_times += 1

        def show_record(self) -> None:
            self._show_times += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_times} grow, {self._age_times}"
                  f" age, {self._show_times} show")

    def __init__(
        self, name: str, height: float, age: int, growth_rate: float
    ) -> None:
        self.name = name.capitalize()
        self.stats = self.Stats()
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
        self.stats.age_record()
        self._age += days

    def grow(self, days: int) -> None:
        self.stats.grow_record()
        self._height += self._growth_rate * days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}:  Error, "
                  f"height can't be negative\nHeight update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, "
                  f"age can't be negative\nAge update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self.stats.show_record()
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self, name: str, height: float,
        age: int, growth_rate: float, color: str
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        print(super().show())
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    stats: "Tree.TreeStats"

    def __init__(
        self, name: str, height: float, age: int,
        growth_rate: float, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self.stats = self.TreeStats()

    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def shade_record(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def produce_shade(self) -> None:
        self.stats.shade_record()
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")

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


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int,
        growth_rate: float, color: str, seeds: int
    ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.seeds = seeds

    def age(self, days: int) -> None:
        super().age(days)

    def grow(self, days: int) -> None:
        super().grow(days)

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def statistics_function(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year?"
          f" -> {Plant.is_older_than_a_year(400)}")
    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, 0.4, "red")
    rose.show()
    statistics_function(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(20)
    rose.bloom()
    rose.show()
    statistics_function(rose)
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 0.5, 5.0)
    oak.show()
    statistics_function(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    statistics_function(oak)
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, 1.5, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    statistics_function(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    statistics_function(unknown)
