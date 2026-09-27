"""Convert a JSON array of objects to CSV using only Python's standard library."""
import argparse
import csv
import json
from pathlib import Path


def convert(source, destination):
    records = json.loads(Path(source).read_text(encoding="utf-8-sig"))
    if not isinstance(records, list) or any(not isinstance(row, dict) for row in records):
        raise ValueError("Input must be a JSON array of objects")
    columns = list(dict.fromkeys(key for row in records for key in row))
    def cell(value):
        if value is None:
            return ""
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
            value = "'" + value
        return value
    with Path(destination).open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output)
        writer.writerow([cell(key) for key in columns])
        writer.writerows([[cell(row.get(key)) for key in columns] for row in records])
    return len(records)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    try:
        count = convert(args.source, args.destination)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Error: {error}\n")
    print(f"Converted {count} records to {args.destination}")
