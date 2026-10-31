if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grime/dark_book.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grime.dark_book as ds
    ds.dark_record("darkness", ["road", "night", "saad"])
