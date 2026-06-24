"""Интерфейс командной строки для CSV-анализатора."""
import sys

from csv_analyzer.reader import read_csv
from csv_analyzer.stats import (average_resolution_time_hours, closed_fraction,
                                count_by_category, count_by_status)


def main():
    if len(sys.argv) < 2:
        print("Использование: python -m csv_analyzer.cli <путь к CSV>")
        sys.exit(1)

    path = sys.argv[1]
    tickets = read_csv(path)

    print(f"Записей обработано: {len(tickets)}")
    print("\nКоличество по статусам:")
    for status, cnt in count_by_status(tickets).items():
        print(f"  {status}: {cnt}")

    print("\nКоличество по категориям:")
    for cat, cnt in count_by_category(tickets).items():
        print(f"  {cat}: {cnt}")

    avg = average_resolution_time_hours(tickets)
    frac = closed_fraction(tickets)
    print(f"\nСреднее время обработки закрытых заявок: {avg:.2f} ч.")
    print(f"Доля закрытых заявок: {frac:.2f}%")


if __name__ == "__main__":
    main()
