import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog
)
from crypto_utils import hash_text, encrypt_aes, decrypt_aes

class CryptoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Tool")
        self.setGeometry(100, 100, 600, 500)
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.input_label = QLabel("Input:")
        self.input_text = QTextEdit()

        self.method_label = QLabel("Method:")
        self.method_combo = QComboBox()
        self.method_combo.addItems(["Hash - SHA256", "Hash - SHA512", "Encrypt - AES", "Decrypt - AES"])

        self.key_label = QLabel("Key (AES only):")
        self.key_input = QLineEdit()
        self.key_input.setEchoMode(QLineEdit.Password)

        self.process_button = QPushButton("Process")
        self.process_button.clicked.connect(self.process_action)

        self.result_label = QLabel("Result:")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        self.logs_button = QPushButton("View Logs")
        self.logs_button.clicked.connect(self.show_logs)

        self.save_result_button = QPushButton("Save Result")
        self.save_result_button.clicked.connect(self.save_result)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_text)
        vbox.addWidget(self.method_label)
        vbox.addWidget(self.method_combo)
        vbox.addWidget(self.key_label)
        vbox.addWidget(self.key_input)
        vbox.addWidget(self.process_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_text)

        hbox = QHBoxLayout()
        hbox.addWidget(self.logs_button)
        hbox.addWidget(self.save_result_button)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def process_action(self):
        input_data = self.input_text.toPlainText().strip()
        method = self.method_combo.currentText()
        key = self.key_input.text().strip()
        
        if not input_data:
            self.result_text.setPlainText("Please enter input text.")
            return

        try:
            if "Hash - SHA256" in method:
                result = hash_text(input_data, "sha256")
            elif "Hash - SHA512" in method:
                result = hash_text(input_data, "sha512")
            elif "Encrypt - AES" in method:
                if not key:
                    self.result_text.setPlainText("Please enter a key for AES encryption.")
                    return
                result = encrypt_aes(input_data, key)
            elif "Decrypt - AES" in method:
                if not key:
                    self.result_text.setPlainText("Please enter a key for AES decryption.")
                    return
                result = decrypt_aes(input_data, key)
            else:
                result = "Unsupported method."
        except Exception as e:
            result = f"Error: {str(e)}"

        self.result_text.setPlainText(result)
        self.log_action(method, input_data, result)

    def log_action(self, method, input_data, result):
        with open("logs.txt", "a", encoding='utf-8') as f:
            f.write(f"Method: {method}\nInput: {input_data}\nResult: {result}\n---\n")

    def show_logs(self):
        try:
            with open("logs.txt", "r", encoding='utf-8') as f:
                logs = f.read()
            self.result_text.setPlainText(logs)
        except FileNotFoundError:
            self.result_text.setPlainText("No logs found.")

    def save_result(self):
        result = self.result_text.toPlainText()
        if not result.strip():
            return
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Result", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CryptoApp()
    window.show()
    sys.exit(app.exec_())
