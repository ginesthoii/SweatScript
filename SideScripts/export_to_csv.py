#!/usr/bin/env python3
import re
import csv
import sys

def export_to_csv(log_file="workouts.log", output_file="workouts.csv"):
    """
    Reads workout data from a log file and exports it to a CSV file.
    """
    data = []
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Use regex to parse the structured log entry
                match = re.search(r'\[(.*?)\] \| (.*?) \| Duration: (.*?) \| Notes: (.*)', line)
                if match:
                    timestamp, workout_type, duration, notes = match.groups()
                    data.append([timestamp.strip(), workout_type.strip(), duration.strip(), notes.strip()])
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.", file=sys.stderr)
        return

    if not data:
        print("No data to export.")
        return

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Workout Type', 'Duration', 'Notes'])  # Write header
        writer.writerows(data)

    print(f"Successfully exported {len(data)} workouts to {output_file}")

if __name__ == "__main__":
    export_to_csv()
