# Description: This program organizes files with '.jpg' and '.pdf' extensions in the current directory by moving them
#              into separate directories named 'images' and 'PDF', respectively.

# Import the necessary modules.
import shutil
from pathlib import Path
import zipfile

# Open the 'files.zip' archive in read mode using the 'ZipFile' class and create a 'zip' object.
zip = zipfile.ZipFile('files.zip')

# Iterate through all the files with the '.jpg' extension in the current directory using 'Path().glob(r'*.jpg')'.
for filename in Path().glob(r'*.jpg'):
    # Print the filename (optional, for demonstration purposes).
    print(filename)

    # Move each '.jpg' file to the 'images' directory using the 'shutil.move()' function.
    shutil.move(filename, 'images')

# Iterate through all the files with the '.pdf' extension in the current directory using 'Path().glob(r'*.pdf')'.
for filename in Path().glob(r'*.pdf'):
    # Print the filename (optional, for demonstration purposes).
    print(filename)

    # Move each '.pdf' file to the 'PDF' directory using the 'shutil.move()' function.
    shutil.move(filename, 'PDF')
