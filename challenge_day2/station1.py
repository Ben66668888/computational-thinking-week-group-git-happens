# Station 1
#
# Observed at the station:
#   input  type: int
#   output type: int
#
# Algorithm: the n-th Fibonacci number, with F(0) = 0, F(1) = 1.
#
# Verified against the station observations:
#   48 -> 4807526976
#   70 -> 190392490709135
#   44 -> 701408733
#   18 -> 2584
# Deduced for the missing outputs:
#   83 -> 99194853094755497
#   25 -> 75025
#   23 -> 28657
#   67 -> 44945570212853

# (input, expected_output) pairs copied from the station
OBSERVATIONS = [
    (48, 4807526976),
    (70, 190392490709135),
    (44, 701408733),
    (18, 2584),
]


def solution_station_1(station1_input: int) -> int:
    """Return the n-th Fibonacci number (F(0) = 0, F(1) = 1)."""
    a, b = 0, 1
    for _ in range(station1_input):
        a, b = b, a + b
    return a