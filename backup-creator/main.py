import os
import shutil

def backup_files(source_dir, backup_dir):
    # Walk through the source directory
    for root, _, files in os.walk(source_dir):
        # Iterate over each file in the current directory
        for file in files:
            # Construct the full path to the source file
            source_file = os.path.join(root, file)
            # Construct the full path to the backup file
            backup_file = os.path.join(backup_dir, root.replace(source_dir, ''), file)

            # Create the directory for the backup file if it doesn't exist
            os.makedirs(os.path.dirname(backup_file), exist_ok=True)
            # Copy the source file to the backup location, preserving metadata
            shutil.copy2(source_file, backup_file)

    # Walk through the backup directory
    for root, _, files in os.walk(backup_dir):
        # Iterate over each file in the current directory
        for file in files:
            # Construct the full path to the backup file
            backup_path = os.path.join(root, file)
            # Construct the full path to the corresponding source file
            source_path = os.path.join(source_dir, root.replace(backup_dir, ''), file)

            # If the source file does not exist, remove the backup file
            if not os.path.exists(source_path):
                os.remove(backup_path)

# Define the source and backup directories
source_dir = '/path/to/source'
backup_dir = '/path/to/backup'

# Call the function to backup files
backup_files(source_dir, backup_dir)