# 🔐 File & Folder Encryption & Decryption Tool 

This project is a powerful tool that can encrypt and decrypt single files or entire directories using the cryptography library with Fernet encryption.

Available both as a Python script and as a Windows EXE.

## ✨ Features

— 🔑 Automatic key generation
— 📁 File or directory mode
— 🔒 AES256-based Fernet encryption
— 🔓 Secure decryption
— 📦 Windows EXE available (no Python needed)
— 🛑 Skips internal files (key_file.txt, main.exe, main.py)
— 📁 Recursive folder scanning
— 🧱 Error handling with clear messages

## 📥 Installation (Windows EXE)
	1.	Download main.exe from the Releases tab.
	2.	Place it anywhere on your system.
	3.	(Optional) Create a desktop shortcut.
	4.	Run it with a double-click.

## Benefits of the EXE version:

- No Python required
- Portable
- Fully offline
- Zero setup


## 📦 Requirements

- Python 3.x  
- `cryptography` library  
  Install with:
```bash
  pip install cryptography
```

### Run

```bash
  python main.py
```

## 🧠 How It Works

```bash
Do you want to process a file or a folder? (f for file / d for directory)
```

- f selects a file
- d select a directory

```bash
   Enter the folder name to create and process files:
```

Make sure the folder/file exists or create it before running the script.

## 2. Choose an Action

You then select:

```bash
    1. encrypt 🔒 
    2. decrypt 🔓
```

- 1 generates a key and encrypts all files inside the selected folder.

- 2 loads the key from key_file.txt and decrypts the files.

## Key Handling 🔑
	•	Encryption generates a new key automatically
	•	You must store it securely


- During encryption, the script writes the generated key to:

```bash
    key_file.txt
```

- Store this key safely.
Without it, decrypting the files is impossible.

## File Collection 📁

All files inside the user-defined folder are scanned recursively.

Ignored files:

- key_file.txt
- main.exe
- main.py

## 5. Encryption / Decryption ⚙️

- Encryption uses Fernet.encrypt()
- Decryption uses Fernet.decrypt()
- Any file-level errors are displayed during processing

## ▶️ Usage

1. Create a folder with any name.
2. Run the script:

```bash
    python main.py
```
3. use folder or file
4. Enter the folder name when prompted.
5. Choose 1 (encrypt) or 2 (decrypt).
6. Keep the key file safe.

## ⚠️ Important Notes
- 🔥 Files cannot be recovered without the correct key
- 🔁 Encrypted files overwrite the originals
- 💾 Always make backups
- 🚫 Do not modify key_file.

## 📜 Disclaimer

This tool uses strong encryption.
The user is responsible for key management.
Losing the key means permanently losing access to encrypted data.
