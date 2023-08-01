# Description: This program is used to add all the files with any extension from the current directory and its subdirectories
#              (except for the 'files.zip' and 'zipCompressed.py' files) to a zip archive named 'files.zip'.

# Import the necessary modules.
from zipfile import ZipFile
from pathlib import Path

# Open the 'files.zip' archive in append mode ('a') using the 'ZipFile' class and create a context manager with 'zip'.
# The context manager ensures that the zip archive is automatically closed after the block execution.
with ZipFile('files.zip', 'a') as zip:
    # Use 'Path().rglob('*.*')' to recursively iterate through all files in the current directory and its subdirectories.
    # 'rglob()' returns a generator that yields all paths matching the pattern ('*.*' matches files with any extension).
    for path in Path().rglob('*.*'):
        # Print the path of each file (optional, for demonstration purposes).
        print(path)

        # Exclude the 'files.zip' and 'zipCompressed.py' files from being added to the zip archive.
        # The 'str(path)' is used to convert the path object to a string for comparison.
        # The 'if' statement checks if the path is not equal to 'files.zip' and also not equal to 'zipCompressed.py'.
        # If both conditions are True, the file will be added to the zip archive. Otherwise, it will be skipped.
        if str(path) != 'files.zip' and str(path) != 'zipCompressed.py':
            # Add the current file to the 'files.zip' archive using the 'write()' method of the 'zip' object.
            zip.write(path)
