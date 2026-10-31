from alchemy import elements
from ..lotions import strength_lotion
from elements import ft_fire


def lead_to_gold() -> str:
    line1 = "Tool transmutation Lead to Gold: brew "
    line2 = f"'[{elements.ft_air()}]' and "
    line3 = f"'[{strength_lotion()}]' mixed with '[{ft_fire()}]'"
    return line1 + line2 + line3
