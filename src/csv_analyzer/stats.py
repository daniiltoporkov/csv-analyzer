from typing import Dict, List, Tuple

from csv_analyzer.reader import Ticket


def count_by_status(tickets: List[Ticket]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for ticket in tickets:
        counts[ticket.status] = counts.get(ticket.status, 0) + 1
    return counts


def count_by_category(tickets: List[Ticket]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for ticket in tickets:
        counts[ticket.category] = counts.get(ticket.category, 0) + 1
    return counts


def average_resolution_time_hours(tickets: List[Ticket]) -> float:
    closed = [t for t in tickets if t.status == "Closed" and t.closed is not None]
    if not closed:
        return 0.0
    total_hours = sum((t.closed - t.created).total_seconds() / 3600 for t in closed)
    return total_hours / len(closed)


def closed_fraction(tickets: List[Ticket]) -> float:
    if not tickets:
        return 0.0
    closed_count = sum(1 for t in tickets if t.status == "Closed")
    return (closed_count / len(tickets)) * 100


# end of stats module
