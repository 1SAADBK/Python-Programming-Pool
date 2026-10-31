from ex0 import FlameFactory, AquaFactory


if __name__ == "__main__":
    ff = FlameFactory()
    af = AquaFactory()
    fl = ff.create_base()
    py = ff.create_evolved()
    ab = af.create_base()
    tg = af.create_evolved()
    print("Testing factory")
    print(fl.describe())
    print(fl.attack())
    print(py.describe())
    print(py.attack())

    print("\nTesting Factory")
    print(ab.describe())
    print(ab.attack())
    print(tg.describe())
    print(tg.attack())

    print("\nTesting battle")
    print(fl.describe())
    print("vs.")
    print(ab.describe())
    print(" fight!")
    print(fl.attack())
    print(ab.attack())
