#!/bin/bash

# Define the log file
LOG_FILE="workouts.log"

# Get the current date and time
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Prompt the user for workout details
echo "--- SweatScript Log Entry ---"
read -p "Workout type (e.g., Running, Lifting, Cycling): " WORKOUT_TYPE
read -p "Duration (e.g., 30 min, 1 hr): " DURATION
read -p "Intensity/Notes: " NOTES

# Write the entry to the log file
echo "[$TIMESTAMP] | $WORKOUT_TYPE | Duration: $DURATION | Notes: $NOTES" >> "$LOG_FILE"

echo "Workout logged successfully to $LOG_FILE"
echo "------------------------------"
