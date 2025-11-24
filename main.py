from cryptography import fernet
from crypto import encrypt_file, decrypt_file
from get_all_files import file_paths, get_all_files_fnc
import os
key = fernet.Fernet.generate_key()
folder_name = None
file_name = None

while True:
    file_or_folder = input("Do you want to process a file or a folder? (f for file / d for directory): ")
    if file_or_folder.lower() == 'f':
        file = True
        folder = False
        file_name = input("Enter the file name to process: ")
        if not os.path.exists(file_name):
            print(f"The file '{file_name}' does not exist. ")
            input("Press Enter to exit...")
            exit()
        print(f"Processing file: {file_name}")
    elif file_or_folder.lower() == 'd':
        file = False
        folder = True
        folder_name = input(f"Enter the folder name to create and process files: ")
        if not os.path.exists(folder_name):
            print(f"The folder '{folder_name}' does not exist. ")
            input("Press Enter to exit...")
            exit()
    else:
        print("Invalid input. Please enter 'f' for file or 'd' for directory.")
        exit()

    print("""Do you want to 
    1.encrypt 
    2.decrypt 
    the files'?
    """)
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        encrypting = True
        decrypting = False
    elif int_choice == 2:
        encrypting = False
        decrypting = True
    else:
        print("Invalid choice. Exiting.")
        exit()
    if encrypting:
        print("You chose to encrypt the files.")
        print("Schlüssel: ", key.decode())
        key_file = open("key_file.txt", "w")
        key_file.write(key.decode())
        print("Please keep the key safe, otherwise this can never be decrypt again.")
    elif decrypting:
        print("You chose to decrypt the files.")
        key_file = open("key_file.txt", "r")
        key_input = key_file.read()
        key = key_input.encode()
    if folder:
        get_all_files_fnc(folder_name)
        for file in file_paths:
            if encrypting:
                encrypt_file(file, key)
            elif decrypting:
                decrypt_file(file, key)
    elif file:
        if encrypting:
            encrypt_file(file_name, key)
        elif decrypting:
            decrypt_file(file_name, key)
    print("Process completed.")
    do_exit = input("Do you want to exit? (y/n): ")
    if do_exit.lower() == 'y':
        break
input("Press Enter to exit...")
