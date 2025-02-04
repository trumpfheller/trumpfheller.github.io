import os

def list_files_in_folder(folder_path):
    # Check if the provided path is a valid directory
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory.")
        return

    # List all files in the directory
    files = os.listdir(folder_path)

    # Print the list of files
    print("Files in directory '{}':".format(folder_path))
    for file_name in files:
        print(file_name)

# Replace 'folder_path' with the path to the directory you want to list the files of
#folder_path = "path/to/your/folder"
folder_path = "/Users/mike/Documents/GitHub/documentation/02_string_listTuple"
list_files_in_folder(folder_path)
