#!/usr/bin/env python3
import argparse

def view_recent_workouts(log_file="workouts.log", count=5):
    """
    Views the most recent workout entries from the log file.
    
    Args:
        log_file (str): The path to the workout log file.
        count (int): The number of recent entries to display.
    """
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No workouts logged yet.")
                return

            print(f"--- Your last {min(count, len(lines))} workouts ---")
            for line in lines[-count:]:
                print(line.strip())
            print("-----------------------------------")
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View recent workout entries.")
    parser.add_argument(
        "-c", "--count", type=int, default=5,
        help="Number of recent entries to show (default: 5)"
    )
    args = parser.parse_args()
    view_recent_workouts(count=args.count)
