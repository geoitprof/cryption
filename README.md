# Hash & Encryption Tool (Python + PyQt5)

A simple, clean GUI-based application for **hashing, encrypting, and decrypting text**, built with **Python**, **PyQt5**, and **PyCryptodome**.

Supports:
- SHA256 & SHA512 hashing
- AES encryption & decryption (with a custom key)
- Logging of all actions
- Saving results to text files
- View logs inside the app

---

## Features

- Clean, user-friendly GUI (PyQt5)
- Input text → choose method → get result
- Supports SHA256, SHA512 hashing
- AES-128 encryption & decryption
- Logs history of all processed actions (`logs.txt`)
- Option to view logs inside the app
- Option to save result to a `.txt` file
- Cross-platform: tested on **Windows** & **Linux (Fedora)**

---

## 🛠️ Dependencies

✅ Install required packages using `pip`:

```bash
pip install PyQt5
pip install pycryptodome
