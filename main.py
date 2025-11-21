from cryptography import fernet
import os

key = fernet.Fernet.generate_key()
folder_name = None
file_name = None

file_or_folder = input("Do you want to process a file or a folder? (f for file / d for directory): ")
if file_or_folder.lower() == 'f':
    file = True
    folder = False
    file_name = input("Enter the file name to process: ")
else:
    file = False
    folder = True
    folder_name = input("Enter the folder name to create and process files: ")

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
file_paths = []

def get_all_files(directory):
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


def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        fernet_instance = fernet.Fernet(key)
        encrypted_data = fernet_instance.encrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
    except Exception as e:
        print(f"An error occurred while encrypting:  {file_path}: {e}")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            decrypted_data = file.read()
        
        fernet_instance = fernet.Fernet(key)
        decrypted_data = fernet_instance.decrypt(decrypted_data)
        
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
    except Exception as e:
        print(f"An error occurred during decryption: {file_path}: {e}")

if folder:
    get_all_files(folder_name)
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
