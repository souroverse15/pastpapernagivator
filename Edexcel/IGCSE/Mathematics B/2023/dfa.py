import os

# Function to determine the new file name based on the old name
def get_new_filename(old_name):
    # Check for Paper 1 or Paper 2
    if "-02-" in old_name or "-02r-" in old_name:
        paper_type = "Paper2"
    elif "-01-" in old_name or "-01r-" in old_name:
        paper_type = "Paper1"
    else:
        return old_name  # If no match, return the original name
    
    # Check for "R" in the name (for Paper1R, Paper2R, etc.)
    if "1r" in old_name or "2r" in old_name:
        paper_type += "R"

    # Rename the file based on the MS or QP match
    if "rms" in old_name:
        return f"MS {paper_type}.pdf"
    elif "que" in old_name:
        return f"QP {paper_type}.pdf"
    else:
        return old_name  # If no match, return the original name

# Get the current working directory
current_directory = os.getcwd()

# Walk through every directory and subdirectory
for dirpath, dirnames, filenames in os.walk(current_directory):
    for file_name in filenames:
        # Check if it's a PDF file
        if file_name.endswith(".pdf"):
            old_path = os.path.join(dirpath, file_name)
            new_name = get_new_filename(file_name)
            
            if new_name != file_name:  # Only rename if the name has changed
                new_path = os.path.join(dirpath, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed '{old_path}' to '{new_path}'")
