class SecurePlant:
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15.0, 10, 1)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-3)
    print()
    print(f"Current state: {rose.show()}")
