import sys
import os
import site


if __name__ == "__main__":
    there_is_an_env = (sys.prefix != sys.base_prefix)
    if there_is_an_env:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"\n Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\activate # On Windows\n\nThen run this "
              "program again.")
