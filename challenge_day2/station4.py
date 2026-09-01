# Station 4
#
# Observed at the station:
#   input type: int
#   output type: bool
#
# Algorithm: Check if the number is a prime number.

OBSERVATIONS = [
    (77, False),
    (87, False),
    (31, True),
    (65, False),
    (39, False),
    (91, False),
    (45, False),
    (26, False),
]

def solution_station_4(station4_input: int) -> bool:
    """Decipher the Station 4 algorithm and return its boolean output."""
    if station4_input < 2:
        return False
    for i in range(2, int(station4_input ** 0.5) + 1):
        if station4_input % i == 0:
            return False
    return True
