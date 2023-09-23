import os
import shutil
import sys

__started__ = """
x-------------------------x
|   File Sorted Manager   |
x-------------------------x
"""

def path_exists(path=None):
    """
    Check if a directory exists, not a file, at the specified path.
    """
    return os.path.exists(path) and not os.path.isfile(path)


def create_directory(file_path, extension):
    """
    A method to creates a directory which is seprated 
    by different file extensions.
    """
    dir_name = extension[1:]
    dir_path = os.path.join(file_path, dir_name)

    if not path_exists(dir_path):
        os.makedirs(dir_path)
    
    return dir_path


def remove_directory(path=None):
    """
    Remove all the empty directory from the given path.
    """

    for root_dir, sub_dir, filenames in os.walk(path):
        for current_dir in sub_dir:
            dir_path = os.path.join(root_dir, current_dir)

            if not os.listdir(dir_path):
                os.rmdir(dir_path)


def get_sort_files(path=None):
    """
    A method for sorts files in the given directory 
    by their extensions.
    """
    # Loop through all files in the directory and its subdirectories.
    for root_dir, sub_dir, filenames in os.walk(path):
        for files in filenames:
            file_path = os.path.join(root_dir, files)
            filename, extension = os.path.splitext(files)
            
            # check if extension in any file then create the directory.
            if extension:
                add_directory = create_directory(path, extension)
                add_new_path = os.path.join(add_directory, files)
                # then move the file to the recently created directory.
                shutil.move(file_path, add_new_path)


def main():
    # Take an input path of the directory from the user.
    input_path = input("Enter your folder path: >>> ")

    if path_exists(path=input_path):
        # sort all files.
        get_sort_files(path=input_path)
        # remove the empty directory.
        remove_directory(path=input_path)
        print("Your files sorted succesfully!")
    else:
        print("Warning: Provide a valid directory path on your computer!", file=sys.stderr)


if __name__ == "__main__":
    print(__started__)
    main()