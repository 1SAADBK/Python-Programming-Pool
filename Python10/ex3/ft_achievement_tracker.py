import random


class Player():
    def __init__(self, name: str, achv: set) -> None:
        self.name = name.capitalize()
        self.achv = achv

    def show_achv(self) -> str:
        return f"Player {self.name}: {self.achv}"


def gen_player_achievements() -> set:
    achv = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
            'Survivor', 'Master Explorer', 'Treasure Hunter',
            'First Steps', 'Collector', 'Sharp Mind',
            'Boss Slayer']
    count = random.randint(0, len(achv))
    return set(random.sample(achv, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players_names = ["alice", "bob", "charlie", "dylan"]
    players = []
    for name in players_names:
        players.append(Player(name, gen_player_achievements()))
    for player in players:
        print(player.show_achv())
    s1, s2 = players[0].achv, players[1].achv
    s3, s4 = players[2].achv, players[3].achv
    all_achv = set.union(s1, s2, s3, s4)
    print(f"\n All distinct achievements: {all_achv}\n")
    print(f"Common achievements: {set.intersection(s1, s2, s3, s4)}\n")
    print(f"Only Alice has: {s1.difference(set.union(s2, s3, s4))}")
    print(f"Only Bob has: {s2.difference(set.union(s1, s3, s4))}")
    print(f"Only Charlie has: {s3.difference(set.union(s1, s2, s4))}")
    print(f"Only Dylan has: {s4.difference(set.union(s1, s2, s3))}\n")
    for p in players:
        missing = all_achv.difference(p.achv)
        print(f"{p.name} is missing: {missing}")
