# Station 6
#
# Observed at the station:
#   input  type: int
#   output type: float
#
# Algorithm: calculated the sine of the input in radians and then
# rounded to 4 decimal places.
#
# Verified against the station observations:
#   39 -> 0.9638
#   78 -> 0.5140
#   44 -> 0.0177
#   77 -> 0.9995
#   84 -> 0.7332
#   32 -> 0.5514
#   17 -> -0.9614
#
# (input, expected_output) pairs copied from the station
import math
#applying trigonometric function in sin, and outcome as angel of radius

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