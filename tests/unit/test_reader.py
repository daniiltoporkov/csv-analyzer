import os
import tempfile

import pytest

from csv_analyzer.reader import read_csv


def test_read_valid_csv():
    data = """id,category,status,created,closed
1,Software,Closed,2026-05-01 10:00:00,2026-05-02 12:00:00
2,Hardware,Open,2026-05-03 09:00:00,
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(data)
        f.flush()
        tickets = read_csv(f.name)
    os.unlink(f.name)
    assert len(tickets) == 2
    assert tickets[0].id == 1
    assert tickets[0].closed is not None
    assert tickets[1].closed is None


def test_read_empty_csv():
    data = "id,category,status,created,closed\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(data)
        f.flush()
        tickets = read_csv(f.name)
    os.unlink(f.name)
    assert len(tickets) == 0


def test_read_missing_file():
    try:
        read_csv("nonexistent.csv")
        assert False, "Должно было возникнуть исключение"
    except FileNotFoundError:
        pass


def test_read_csv_missing_required_column():
    data = """id,category,created,closed
1,Software,2026-05-01 10:00:00,
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(data)
        f.flush()
        with pytest.raises(KeyError):
            read_csv(f.name)
    os.unlink(f.name)


def test_read_csv_invalid_date():
    data = """id,category,status,created,closed
1,Software,Closed,01-05-2026 10:00:00,
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(data)
        f.flush()
        with pytest.raises(ValueError):
            read_csv(f.name)
    os.unlink(f.name)
