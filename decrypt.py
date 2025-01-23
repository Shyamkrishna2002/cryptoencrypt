
from cryptography.fernet import Fernet

def decrypt_message():
    # Input the key
    key = input("Enter the decryption key: ").strip().encode()

    # Initialize Fernet with the key
    try:
        fernet = Fernet(key)
    except ValueError:
        print("Error: Invalid key format. Ensure it's base64-encoded.")
        return

    # Input the cipher text
    encrypted_message = input("Enter the encrypted message (cipher): ").strip().encode()

    # Attempt to decrypt the message
    try:
        decrypted_message = fernet.decrypt(encrypted_message)
        print("Decrypted Message:", decrypted_message.decode())
    except Exception as e:
        print("Error: Decryption failed. The key or cipher text is incorrect.")

if __name__ == "__main__":
    decrypt_message()
