from cryptography import fernet
from crypto import encrypt_file, decrypt_file
from get_all_files import file_paths, get_all_files_fnc
import os

key = None  # Initialize key globally
folder_name = None
file_name = None
decrypting = False
encrypting = False
input_choice = "None"
int_choice = None
key = None

def folder_or_file():
    global folder_name, file_name  # Declare global variables
    print("""Do you want to 
    1. work with a folder 
    2. work with a single file?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        folder = True
        file = False
        folder_name = input("Enter the folder path: ")
    elif int_choice == 2:
        folder = False
        file = True
        file_name = input("Enter the file path: ")
    else:
        print("Invalid choice. Exiting.")
        exit()
    return folder, file

def encrypting_or_decrypting():
    global encrypting, decrypting, key  # Declare global variables
    print("""Do you want to 
    1.encrypt 
    2.decrypt 
    the files'?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        encrypting = True
        decrypting = False
        key = fernet.Fernet.generate_key()  # Generate key for encryption
    elif int_choice == 2:
        encrypting = False
        decrypting = True
        try:
            with open("key_file.txt", "r") as key_file:
                key = key_file.read().encode()  # Read key for decryption
        except FileNotFoundError:
            print("Key file not found. Cannot decrypt.")
            exit()
    else:
        print("Invalid choice. Exiting.")
        exit()

def main():
    global key, folder_name  # Ensure global variables are used
    folder, file = folder_or_file()
    encrypting_or_decrypting()
    if key is None:  # Check if key is properly initialized
        print("Error: Key is not initialized. Exiting.")
        exit()
    if encrypting:
        print("You chose to encrypt the files.")
        print("Schlüssel: ", key.decode())
        with open("key_file.txt", "w") as key_file:
            key_file.write(key.decode())
        print("Please keep the key safe, otherwise this can never be decrypted again.")
    elif decrypting:
        print("You chose to decrypt the files.")
        key_file = open("key_file.txt", "r")
        key_input = key_file.read()
        key = key_input.encode()
    if folder:
        if not folder_name:  # Ensure folder_name is not None
            print("Error: Folder name is not set. Exiting.")
            exit()
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
 
if __name__ == "__main__":   
    while True:
        main()
        do_exit = input("Do you want to exit? (y/n): ")
        if do_exit.lower() == 'y':
            break  


input("Press Enter to exit...")
