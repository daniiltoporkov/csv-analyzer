from datetime import datetime, timedelta

from csv_analyzer.reader import Ticket
from csv_analyzer.stats import (average_resolution_time_hours, closed_fraction,
                                count_by_category, count_by_status)

tickets = [
    Ticket(
        1,
        "Hardware",
        "Closed",
        datetime(2026, 5, 1, 10, 0, 0),
        datetime(2026, 5, 1, 14, 0, 0),
    ),
    Ticket(2, "Software", "Open", datetime(2026, 5, 2, 9, 0, 0), None),
    Ticket(
        3,
        "Hardware",
        "Closed",
        datetime(2026, 5, 3, 11, 0, 0),
        datetime(2026, 5, 3, 15, 0, 0),
    ),
    Ticket(4, "Network", "In Progress", datetime(2026, 5, 4, 8, 0, 0), None),
    Ticket(
        5,
        "Software",
        "Closed",
        datetime(2026, 5, 5, 12, 0, 0),
        datetime(2026, 5, 6, 12, 0, 0),
    ),
]


def test_count_by_status():
    res = count_by_status(tickets)
    assert res == {"Closed": 3, "Open": 1, "In Progress": 1}


def test_count_by_category():
    res = count_by_category(tickets)
    assert res == {"Hardware": 2, "Software": 2, "Network": 1}


def test_average_resolution_time():
    avg = average_resolution_time_hours(tickets)
    # три закрытых: 4h, 4h, 24h => average = 32/3 ≈ 10.666...
    assert abs(avg - 10.6666666) < 0.1


def test_closed_fraction():
    frac = closed_fraction(tickets)
    assert abs(frac - 60.0) < 0.01


def test_empty_tickets():
    assert count_by_status([]) == {}
    assert count_by_category([]) == {}
    assert average_resolution_time_hours([]) == 0.0
    assert closed_fraction([]) == 0.0
