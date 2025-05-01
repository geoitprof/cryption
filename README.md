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

## 🛠Dependencies

Install required packages using `pip`:

````
pip install PyQt5
pip install pycryptodome
````

### Installation

1. Make sure Python 3.x is installed.
2. Clone or download this repository.
3. Navigate to the project folder:
````
cd ~/crypto_app
````
4. Run the app:
````
python main.py
````
(or python3 main.py depending on your system)
The GUI will launch.

## How to Use
1. Enter text in the input box.
2. Choose an operation from the dropdown:
- Hash - SHA256
- Hash - SHA512
- Encrypt - AES
- Decrypt - AES
3. (AES only) Enter a password/key in the Key field.
4. Click Process → result will display.

5. Optionally:
View Logs → displays all past actions
Save Result → saves current result to a text file
All actions are logged automatically to logs.txt.
