import os
import platform
import sys

if platform.system() != "Windows":
    print("I only work on windows, soz")
    print("You are welcome to submit a PR for another operating system.")
    input("Press enter to exit...")
    sys.exit()


def get_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_file_creationdate(absolute_file_path, type_is_creation: bool):
    if type_is_creation:
        return os.path.getctime(absolute_file_path)
    return os.path.getmtime(absolute_file_path)


def epoch_to_datetime(epoch_time):
    from datetime import datetime
    return datetime.fromtimestamp(epoch_time).strftime("%Y%m%dT%H%M%S")

def rename_file(original_absolute_path, new_absolute_path):
    return os.rename(original_absolute_path, new_absolute_path)


def main():
    print("Please enter c for creation date or m for modification date")
    type_is_creation = False
    date_type = input("c or m: ")
    if date_type == "c":
        type_is_creation = True
    print("Please specify full target directory path as text")
    input_directory = input("dir: ")
    file_paths = []
    for file in get_files(input_directory):
        original_file_path = input_directory + "\\" + file
        new_file_path = f"{input_directory}\\{epoch_to_datetime(get_file_creationdate(original_file_path, type_is_creation))}_{file}"
        file_paths.append([original_file_path, new_file_path])
        # print(f"{original_file_path} --> {new_file_path}")
    for file in file_paths:
        print(f"{file[0]} --> {file[1]}")
    print("Ready to rename files. Remember, there is NO undo button. Yet.")
    proceed = input("Enter 'yarp' to rename files: ")
    if proceed != "yarp":
        sys.exit()
    for file in file_paths:
        rename_file(file[0], file[1])
    print("Propa job!")
    sys.exit()

if __name__ == '__main__':
    main()
