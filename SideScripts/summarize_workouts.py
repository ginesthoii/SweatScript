#!/usr/bin/env python3
import re
from collections import defaultdict

def summarize_workouts(log_file="workouts.log"):
    """Reads a log file and provides a summary of workout activity."""
    workout_counts = defaultdict(int)
    total_workouts = 0

    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Regex to extract the workout type from the log entry
                match = re.search(r'\|\s+([^|]+?)\s+\|', line)
                if match:
                    workout_type = match.group(1).strip()
                    workout_counts[workout_type] += 1
                    total_workouts += 1
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
        return

    print("--- SweatScript Workout Summary ---")
    if total_workouts == 0:
        print("No workouts logged yet.")
    else:
        print(f"Total workouts logged: {total_workouts}\n")
        print("Breakdown by workout type:")
        for workout, count in sorted(workout_counts.items(), key=lambda item: item[1], reverse=True):
            print(f"- {workout}: {count}")
    print("-----------------------------------")

if __name__ == "__main__":
    summarize_workouts()