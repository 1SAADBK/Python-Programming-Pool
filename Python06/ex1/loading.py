import importlib.metadata


def check_packages() -> list[tuple[str, bool]]:
    print("Checking dependencies:")
    packages = ["pandas", "numpy", "matplotlib"]
    states = []
    for package in packages:
        try:
            version = importlib.metadata.version(package)
            states.append((f"[OK] {package} ({version})", True))
        except importlib.metadata.PackageNotFoundError:
            states.append((f"[MISSING] {package}", False))
    return states


def ft_analyse() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    print("\nAnalyzing Matrix data...")
    data = np.random.standard_normal(1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(data, columns=['Signal'])
    print("Generating visualization...")
    plt.hist(df['Signal'], bins=30, color='green', alpha=0.7)
    plt.title("Matrix Signal Distribution")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete! Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    missing = False
    states = check_packages()
    for state in states:
        print(state[0])
        if not state[1]:
            missing = True
    if missing:
        print("some packages are missing run <pip install -r "
              "requirements.txt> or <poetry install>")
    else:
        ft_analyse()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error happend: {e}")
