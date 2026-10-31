def validate_grime(grime: list) -> str:
    from . import light_book
    allowed = light_book.light_allowed_book()
    valid = 0
    for item in grime:
        if item in allowed or item.capitalize() in allowed:
            valid = 1
    if valid:
        message = "VALID"
    else:
        message = "INVALID"
    if valid:
        return (f"book recorded: ({grime[0]}, "
                f"{grime[1]} and {grime[2]} - {message})")
    else:
        return (f"book not recorded: ({grime[0]},"
                f" {grime[1]} and {grime[2]} - {message})")
