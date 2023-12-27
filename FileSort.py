import os
import sys
import shutil

def organize_files(source_dir):
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the 'Result' directory at the same level as the source directory
    result_dir = os.path.join(os.path.dirname(source_dir), 'Result')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    # Iterate through all files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Get the full path of the current file
            file_path = os.path.join(root, file)

            # Get the file extension
            _, extension = os.path.splitext(file)

            # Skip files without extensions
            if not extension:
                continue

            # Remove the leading dot from the extension
            extension = extension[1:]

            # Create a directory for the extension if it doesn't exist
            extension_dir = os.path.join(result_dir, f'File {extension.upper()}')
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            # Move the file to the corresponding extension directory
            shutil.move(file_path, os.path.join(extension_dir, file))
            print(f"Moved '{file_path}' to '{extension_dir}'.")

if __name__ == "__main__":
    # Check if the source directory is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/source")
        sys.exit(1)

    # Get the source directory from the command-line argument
    source_directory = sys.argv[1]

    # Run the organizing function
    organize_files(source_directory)
