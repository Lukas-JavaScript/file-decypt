from cryptography import fernet
import os

key = fernet.Fernet.generate_key()

print("Schlüssel: ", key.decode())
key_file = open("key_file.txt", "w")
key_file.write(key.decode())
print("Den Schlüssel bitte gut aufheben, denn sonst kann das hier nie wieder entschlüsselt werden.")
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


get_all_files("neuer_ordner")
for file in file_paths:
    encrypt_file(file, key)
