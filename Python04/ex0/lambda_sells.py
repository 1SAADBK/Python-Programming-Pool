def artifact_sorted(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mazes: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mazes))


def sell_transformer(sells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", sells))


def maze_stats(mazes: list[dict]) -> dict:
    return {"max_power": max(mazes, key=lambda x: x["power"])["power"],
            "min_power": min(mazes, key=lambda x: x["power"])["power"],
            "avg_power": round(sum(list(map(lambda x: x["power"], mazes)))
                               / len(mazes))}


if __name__ == "__main__":
    try:
        print("\nTesting artifact sorter...")
        pickaxe = {"name": "pickaxe",
                   "power": 92,
                   "type": "pickaxe"}
        shovel = {"name": "shovel",
                  "power": 85,
                  "type": "shovel"}
        not_sorted = [pickaxe, shovel]
        sorted_descending = artifact_sorted(not_sorted)
        print(f"{sorted_descending[0]['name']}"
              f" ({sorted_descending[0]['power']}"
              f" power) comes before {sorted_descending[1]['name']} "
              f"({sorted_descending[1]['power']} power)")
        print("\n testing sell transformer")
        sell_names = ["apple", "orange", "pineapple"]
        new_sell_names = sell_transformer(sell_names)
        print(f"{new_sell_names[0]} {new_sell_names[1]} {new_sell_names[2]}")
    except Exception as e:
        print(f"ERROR : {e}")
