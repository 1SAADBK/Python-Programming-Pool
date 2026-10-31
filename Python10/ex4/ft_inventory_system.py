import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict = {}
    for arg in sys.argv[1:]:
        if ":" in arg:
            key = arg.split(":")[0]
            invalid = False
            for item in inventory:
                if item == key:
                    print(f"Redundant item '{key}' - discarding")
                    invalid = True
            if not invalid:
                value_str = arg.split(":")[1]
                try:
                    value = int(value_str)
                    inventory[key] = value
                except ValueError as e:
                    print(f"Quantity error for '{key}': {e}")
        else:
            print(f"Error - invalid parameter '{arg}'")
    print(f"Gor inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    quantity = 0
    for item in inventory:
        quantity += inventory[item]
    print(f"Total quantity of the {len(inventory)} items: {quantity}")
    for item in inventory:
        print(f"Item {item} represents"
              f" {round((inventory[item] / quantity) * 100, 1)}%")
    if len(sys.argv) > 1:
        max_value = 0
        for item in inventory:
            if inventory[item] >= max_value:
                max_value = inventory[item]
                max_key = item
        min_value = max_value
        for item in inventory:
            if inventory[item] <= min_value:
                min_value = inventory[item]
                min_key = item
        print(f"Item most abundant: {max_key} with quantity {max_value}")
        print(f"Item most abundant: {min_key} with quantity {min_value}")
    inventory.update({"new_item": 1})
    print(f"Updated inventory {inventory}")
