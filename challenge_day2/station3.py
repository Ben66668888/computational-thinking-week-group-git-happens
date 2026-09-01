# Station 3
#
# Observed at the station:
#   input  type: int
#   output type: bool
#
# TODO: replace the sample observations below with what you see at the station,
#       then work out the rule that maps input -> output.
# Seeing if the number could be divided by 3 evenly

# (input, expected_output) pairs copied from the station
OBSERVATIONS = [
    (31, False),
    (99, True),
    (64, False),
    (43, False),
    (51, True),
]

# Rule: the output is True exactly when the input is divisible by 3.
#   31 -> 3+1 = 4   -> not divisible by 3 -> False
#   99 -> 9+9 = 18  -> divisible by 3     -> True
#   64 -> 6+4 = 10  -> not divisible by 3 -> False
#   43 -> 4+3 = 7   -> not divisible by 3 -> False
#   51 -> 5+1 = 6   -> divisible by 3     -> True


def solution_station_3(station3_input: int) -> bool:
    """Decipher the Station 3 algorithm and return its boolean output."""
    return station3_input % 3 == 0
