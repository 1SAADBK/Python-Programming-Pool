class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    valid_plants = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    invalid_plants = [
        "Tomato",
        "lettuce"
    ]
    inputs = [valid_plants, invalid_plants]
    i = 0
    message = [
        "Testing valid plants...",
        "Testing invalid plants.."
    ]
    while i < 2:
        print(message[i])
        print("Opening watering system")
        try:
            for plant in inputs[i]:
                water_plant(plant)
        except PlantError as e:
            print(f"Caught PlantError: {e}\n"
                  f".. ending tests and returning to main")
        finally:
            print("Closing watering system\n")
        i += 1
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
