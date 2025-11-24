from cryptography import fernet

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
        input("Press Enter to exit...")
        exit()

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
        input("Press Enter to exit...")
        exit()

