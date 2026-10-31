import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            fileobj: typing.IO = open(sys.argv[1], 'r')
            print("---\n")
            for line in fileobj:
                print(line, end='')
            print("\n\n---")
            fileobj.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}: {e}'")


if __name__ == "__main__":
    main()
