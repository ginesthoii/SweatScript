#!/bin/bash
# A simple script to back up your workout log file.

# Check if the log file exists
LOG_FILE="workouts.log"
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: Log file '$LOG_FILE' not found. Nothing to backup."
    exit 1
fi

# Get the current date for the backup file name
BACKUP_DATE=$(date +"%Y-%m-%d")
BACKUP_FILE="workouts-backup-$BACKUP_DATE.tar.gz"

# Create the compressed tar archive
tar -czf "$BACKUP_FILE" "$LOG_FILE"

echo "Backup of '$LOG_FILE' created as '$BACKUP_FILE'."
