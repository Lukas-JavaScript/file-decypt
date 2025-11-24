import os

file_paths = []

def get_all_files_fnc(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if (
                    file == "key_file.txt"
                    or file == "main.exe"
                    or file == "main.py"
                ):
                    continue
                file_paths.append(os.path.join(root, file))
        return file_paths
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e}")
        input("Press Enter to exit...")
        exit()