from .elements import ft_air, ft_earth
from elements import ft_fire, ft_water


def healing_lotion() -> str:
    return f"Healing lotion brewed with '[{ft_earth()}]' and '[{ft_air()}]'"


def strength_lotion() -> str:
    return f"strength lotion brewed with '[{ft_fire()}]' and '[{ft_water()}]'"
