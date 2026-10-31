def light_allowed_book() -> list:
    return ["sun", "bulb", "flash_light"]


def light_record(ligth_name: str, grime: list) -> str:
    from . import light_validator as lv
    return lv.validate_grime(grime)
