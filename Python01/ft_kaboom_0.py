from alchemy.grime import light_book


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grime module directly")
    print("Testing record light book: "
          f"{light_book.light_record("light", ["sun", "chair", "room"])}")
