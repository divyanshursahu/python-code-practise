import os

# Function to recursively delete files with .log extension
def delete_log_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

# Specify the folder path where the deletion should occur
folder_path = "/path/to/folder"

# Call the function to delete .log files in the folder and subfolders
delete_log_files(folder_path)
