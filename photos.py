import os
import glob
import json
import shutil
from datetime import datetime, timedelta

# Function to get all unique file extensions, excluding .json
def get_extensions(exclude_ext='.json'):
    extensions = set()
    for root, dirs, files in os.walk('.'):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext.lower() != exclude_ext.lower():
                extensions.add(ext)
    return sorted(extensions, reverse=True)

# Function to update the last modified time of a file
def update_file_timestamp(file_path, timestamp):
    unix_epoch = datetime(1970, 1, 1)
    new_time = unix_epoch + timedelta(seconds=int(timestamp))
    os.utime(file_path, (new_time.timestamp(), new_time.timestamp()))

# Function to move a file to the current working directory
def move_file_to_cwd(file_path):
    destination_path = os.path.join(os.getcwd(), os.path.basename(file_path))
    shutil.move(file_path, destination_path)

# Main logic
extensions = get_extensions()
cwd = os.getcwd()

for ext in extensions:
    # Find all files with the current extension
    file_list = [y for x in os.walk('.') for y in glob.glob(os.path.join(x[0], '*'+ext))]
    for file_path in file_list:
        json_file_path = file_path + '.json'
        # Check if the corresponding JSON file exists
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                try:
                    data = json.load(json_file)
                    # Check if the data is a dictionary with the expected keys
                    if isinstance(data, dict) and 'photoTakenTime' in data and 'timestamp' in data['photoTakenTime']:
                        timestamp = data['photoTakenTime']['timestamp']
                        update_file_timestamp(file_path, timestamp)
                    else:
                        print(f"JSON structure is not as expected in {json_file_path}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {json_file_path}: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred while processing {json_file_path}: {e}")
        # Move the file to the current working directory
        if os.path.abspath(file_path) != os.path.join(cwd, os.path.basename(file_path)):
            move_file_to_cwd(file_path)
