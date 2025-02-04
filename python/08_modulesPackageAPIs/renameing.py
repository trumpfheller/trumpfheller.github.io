import os

def rename_md_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Iterate through each file
    for file_name in files:
        # Check if the file ends with ".md"
        if file_name.endswith(".md"):
            # Remove the 'lec_' characters from the file name
            new_name = file_name.replace("lec_", "")
            
            # Construct the new path
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {file_name} to {new_name}")

# Provide the directory path containing the .md files
directory_path = "/Users/mike/Documents/GitHub/documentations/08_modulesPackageAPIs"
rename_md_files(directory_path)
