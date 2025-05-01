from crypto_utils import hash_text, encrypt_aes, decrypt_aes

def log_action(action, input_data, result, method):
    with open("logs.txt", "a") as log_file:
        log_file.write(f"Action: {action}\nMethod: {method}\nInput: {input_data}\nResult: {result}\n---\n")

def show_logs():
    try:
        with open("logs.txt", "r") as log_file:
            print("\n=== History Logs ===")
            print(log_file.read())
    except FileNotFoundError:
        print("No logs found.")

def main():
    while True:
        print("\n--- Crypto Tool ---")
        print("1. Hash Text")
        print("2. Encrypt Text (AES)")
        print("3. Decrypt Text (AES)")
        print("4. Show Logs")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            text = input("Enter text to hash: ")
            algo = input("Algorithm (sha256/sha512): ").lower()
            result = hash_text(text, algo)
            print(f"Hashed Result ({algo}): {result}")
            log_action("Hash", text, result, algo)

        elif choice == '2':
            text = input("Enter text to encrypt: ")
            key = input("Enter encryption key: ")
            result = encrypt_aes(text, key)
            print(f"Encrypted Text: {result}")
            log_action("Encrypt", text, result, "AES")

        elif choice == '3':
            enc_text = input("Enter encrypted text: ")
            key = input("Enter decryption key: ")
            try:
                result = decrypt_aes(enc_text, key)
                print(f"Decrypted Text: {result}")
                log_action("Decrypt", enc_text, result, "AES")
            except Exception as e:
                print("Decryption failed:", e)

        elif choice == '4':
            show_logs()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
