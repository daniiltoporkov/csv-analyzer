import csv
<<<<<<< HEAD
import logging
=======
import os
>>>>>>> master
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Ticket:
    id: int
    category: str
    status: str
    created: datetime
    closed: Optional[datetime] = None


def read_csv(path: str) -> List[Ticket]:
    """Читает CSV-файл и возвращает список объектов Ticket."""
    tickets = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            created = datetime.strptime(row["created"], "%Y-%m-%d %H:%M:%S")
            closed = None
            if row.get("closed"):
                closed = datetime.strptime(row["closed"], "%Y-%m-%d %H:%M:%S")
            ticket = Ticket(
                id=int(row["id"]),
                category=row["category"],
                status=row["status"],
                created=created,
                closed=closed,
            )
            tickets.append(ticket)
    return tickets
