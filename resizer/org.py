import os
import shutil
# Get the list of files in both directories
dir1_files = set(os.listdir('../openAI/imageTest'))
dir2_files = set(os.listdir('images'))

# Find the files that are in both directories
common_files = dir1_files & dir2_files

for filename in common_files:
    old_path = os.path.join('images', filename)
    new_path = os.path.join('diff', filename)
    shutil.move(old_path, new_path)