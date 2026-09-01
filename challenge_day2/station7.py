# Station 7
#
# Observed at the station:
#   input type: str (e.g. "b+c*e+a")
#   output type: float
#
# Parse and evaluate an arithmetic expression given as a string, 
# with variables bound to fixed values — a tiny expression interpreter
#
# Algorithm: Evaluate algebraic expression with fixed variable values:
#   a = 3, b = -1, c = 4, d = 7, e = 0.5

OBSERVATIONS = [
    ("b+c*e+a", 4.0),
    ("c*b+a", -1.0),
    ("a+d*c", 31.0),
    ("b+c+e*a", 4.5),
    ("a*e*b*c", -6.0),
    ("d+e*c", 9.0),
    ("b*c*e", -2.0),
]

def solution_station_7(station7_input: str) -> float:
    """Decipher the Station 7 algorithm and return its float output."""
    context = {
        'a': 3.0,
        'b': -1.0,
        'c': 4.0,
        'd': 7.0,
        'e': 0.5
    }
    return float(eval(station7_input, {}, context))
print(solution_station_7("b+c*e+a"))
print(solution_station_7("c*b+a"))