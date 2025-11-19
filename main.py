from cryptography import fernet
import os

key = fernet.Fernet.generate_key()

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
    print("You chose to decrypt the files.")
    print("Schlüssel: ", key.decode())
    key_file = open("key_file.txt", "w")
    key_file.write(key.decode())
    print("Den Schlüssel bitte gut aufheben, denn sonst kann das hier nie wieder entschlüsselt werden.")
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
        print(f"Beim Verschlüsseln ist ein Fehler aufgetreten {file_path}: {e}")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            decrypted_data = file.read()
        
        fernet_instance = fernet.Fernet(key)
        decrypted_data = fernet_instance.decrypt(decrypted_data)
        
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
    except Exception as e:
        print(f"Beim Entschlüsseln ist ein Fehler aufgetreten {file_path}: {e}")


get_all_files("neuer_ordner")
for file in file_paths:
    encrypt_file(file, key)
    decrypt_file(file, key)
