"""Интерфейс командной строки с JSON-экспортом."""
import json
import sys

from csv_analyzer.reader import read_csv
from csv_analyzer.stats import (average_resolution_time_hours, closed_fraction,
                                count_by_category, count_by_status)


def main():
    if len(sys.argv) < 2:
        print("Использование: python -m csv_analyzer.cli <путь к CSV> [--json]")
        sys.exit(1)

    path = sys.argv[1]
    tickets = read_csv(path)

    stats = {
        "total": len(tickets),
        "by_status": count_by_status(tickets),
        "by_category": count_by_category(tickets),
        "avg_hours": average_resolution_time_hours(tickets),
        "closed_percent": closed_fraction(tickets),
    }

    # Если указан флаг --json, выводим JSON
    if len(sys.argv) == 3 and sys.argv[2] == "--json":
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    else:
        print(f"Записей обработано: {stats['total']}")
        print("\nКоличество по статусам:")
        for status, cnt in stats["by_status"].items():
            print(f"  {status}: {cnt}")
        print("\nКоличество по категориям:")
        for cat, cnt in stats["by_category"].items():
            print(f"  {cat}: {cnt}")
        print(f"\nСреднее время обработки закрытых заявок: {stats['avg_hours']:.2f} ч.")
        print(f"Доля закрытых заявок: {stats['closed_percent']:.2f}%")


if __name__ == "__main__":
    main()
