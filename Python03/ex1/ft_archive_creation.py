import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return
    print("\nTransform data:")
    try:
        fileobj = open(sys.argv[1], 'r')
        transformed = ""
        print("---\n")
        for line in fileobj:
            transformed_line = line.rstrip('\n') + "#\n"
            print(transformed_line, end='')
            transformed += transformed_line
        print("\n---")
        fileobj.close()
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return
    new_file = input("Enter new file name (or empty): ")
    if new_file == "":
        print("Not saving data.")
    else:
        try:
            print(f"Saving data to '{new_file}'")
            out_file: typing.IO = open(new_file, 'w')
            out_file.write(transformed)
            out_file.close()
            print(f"Data saved in file '{new_file}'.")
        except Exception as e:
            print(f"Error saving file: {e}")


if __name__ == "__main__":
    main()
