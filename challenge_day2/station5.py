# Station 5
#
# Observed at the station:
#   input  type: str  (a name, e.g. 'Maliah')
#   output type: int
#
# TODO: replace the sample observations below with what you see at the station,
#       then work out the rule that maps input -> output.

# (input, expected_output) pairs copied from the station
OBSERVATIONS = [
    ("Nicolas", 3),
    ("Sara", 2),
]


def solution_station_5(station5_input: str) -> int:
    vowels = "aeiou"
    return sum(1 for char in station5_input.lower() if char in vowels)


# Test the observations
for name, expected in OBSERVATIONS:
    result = solution_station_5(name)
    print(name, "->", result, "(expected:", expected, ")")