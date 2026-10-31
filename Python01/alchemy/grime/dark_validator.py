from .dark_book import dark_allowed_book


def validate_grime(grime: list) -> str:
    allowed = dark_allowed_book()
    valid = 0
    for item in grime:
        if item in allowed or item.capitalize() in allowed:
            valid = 1
    if valid:
        message = "VALID"
        return (f"book recorded: ({grime[0]}, "
                f"{grime[1]} and {grime[2]} - {message})")
    else:
        message = "INVALID"
        return (f"book not recorded: ({grime[0]}, "
                f"{grime[1]} and {grime[2]} - {message})")
