import os

source = "file.txt"
dest = "new_file.txt"

os.rename(source, dest)
print("Source path renamed to destination path successfully!")
