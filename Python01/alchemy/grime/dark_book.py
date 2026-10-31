from .dark_validator import validate_grime


def dark_allowed_book() -> list:
    return ["night", "deep_ocean", "space"]


def dark_record(dark_name: str, grime: list) -> str:
    return validate_grime(grime)
