
def solution_station_6(station6_input: int) -> float:
    """Decipher the Station 6 algorithm and return its float output."""
    raise NotImplementedError("Station 6 algorithm not deciphered yet")


import math

OBSERVATIONS = [
    (39, 0.9638),
    (78, 0.5140),
    (44, 0.0177),
    (77, 0.9995),
    (84, 0.7332),
    (32, 0.5514),
    (17, -0.9614),
]


def solution_station_6(station6_input: int) -> float:
    """Decipher the Station 6 algorithm and return its float output."""
    return round(math.sin(station6_input), 4)