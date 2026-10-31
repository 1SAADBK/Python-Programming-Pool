from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, NotValidStrategy)


def ft_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    n = len(opponents)
    print(f"{n} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                f1 = opponents[i][0]
                f2 = opponents[j][0]
                c1, s1 = f1.create_base(), opponents[i][1]
                c2, s2 = f2.create_base(), opponents[j][1]
                print("\n* Battle *")
                print(c1.describe())
                print(" vs.")
                print(c2.describe())
                print(" now fight!")
                s1.act(c1)
                s2.act(c2)
    except NotValidStrategy as e:
        print(e)


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    hf = HealingCreatureFactory()
    tf = TransformCreatureFactory()
    ns = NormalStrategy()
    ags = AggressiveStrategy()
    ds = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    ft_battle([(ff, ns), (hf, ds)])
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    ft_battle([(ff, ags), (hf, ds)])
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    ft_battle([(af, ns), (hf, ds), (tf, ags)])
