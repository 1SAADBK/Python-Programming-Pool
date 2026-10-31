import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing ft_air: {alchemy.ft_air()}")
    print("Now show that not all functions can be reached")
    print(f"Testing the hidden ft_earth: {alchemy.ft_earth()}")
