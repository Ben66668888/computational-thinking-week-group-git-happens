# Station 2
#
# Observed at the station:
#   input  type: str  (an ISO date, e.g. '1990-01-01')
#   output type: str  (the weekday, written as a Japanese kanji)
#
# Algorithm: take the day of the week for the given date and return it as the
# single Japanese kanji used for that weekday:
#   Mon 月 / Tue 火 / Wed 水 / Thu 木 / Fri 金 / Sat 土 / Sun 日
#--> Algorithm is based of the calendar to see the date
# Verified against the station observations (recorded here in English):
#   2023-08-05 -> Sat (土)
#   2023-10-30 -> Mon (月)
#   2023-02-14 -> Tue (火)
#   2023-10-07 -> Sat (土)
#   2023-12-13 -> Wed (水)
# Deduced for the missing outputs:
#   2024-11-05 -> 火 (Tue)
#   2024-05-22 -> 水 (Wed)
#   2024-05-19 -> 日 (Sun)
#   2024-03-20 -> 水 (Wed)
#   2024-12-30 -> 月 (Mon)

from datetime import date

# (input, expected_output) pairs copied from the station
OBSERVATIONS = [
    ('2023-08-05', '土'),
    ('2023-10-30', '月'),
    ('2023-02-14', '火'),
    ('2023-10-07', '土'),
    ('2023-12-13', '水'),
]

# Monday .. Sunday, matching datetime.date.weekday()
_WEEKDAY_KANJI = ['月', '火', '水', '木', '金', '土', '日']


def solution_station_2(station2_input: str) -> str:
    """Return the weekday of the given ISO date as a Japanese kanji."""
    return _WEEKDAY_KANJI[date.fromisoformat(station2_input).weekday()]
