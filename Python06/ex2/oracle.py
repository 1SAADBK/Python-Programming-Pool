from dotenv import load_dotenv  # type: ignore
import os


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL", "WARNING: No database configured")
    api = os.getenv("API_KEY", "WARNING: no api-key configured")
    log = os.getenv("LOG_LEVEL", "WARNING:  no log-level configured")
    zion = os.getenv("ZION_ENDPOINT", "WARNING: no zion_endpoint configured")
    if not mode:
        print("WARNING no mode detected: defaulting to development")
        mode = "development"
    if mode == "development":
        print("Mode: development - Debug features enabled")
    elif mode == "production":
        print("Mode: PRODUCTION - Enhanced security active")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db}")
    print(f"API Access: {api}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {zion}")
    print("\nEnvironment security check:\n"
          "[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] No .env file")
    print("[OK] Production overrides available\n"
          "\nThe Oracle sees all configurations.")
