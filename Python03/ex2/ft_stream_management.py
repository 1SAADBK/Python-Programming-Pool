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
            print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
                  file=sys.stderr)
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
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return
    print("Enter new file name (or empty): ", end='')
    sys.stdout.flush()
    new_file = sys.stdin.readline().rstrip("\n")
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
            print("[STDERR] Error opening file "
                  f"'{new_file}': {e}", file=sys.stderr)
            print("Data not saved.")


if __name__ == "__main__":
    main()
