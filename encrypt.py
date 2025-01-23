from cryptography.fernet import Fernet

def encrypt_message():
    # Generate a random key
    key = Fernet.generate_key()
    print("Generated Key (save this to decrypt):", key.decode())

    # Initialize Fernet with the key
    fernet = Fernet(key)

    # Input the message to encrypt
    message = input("Enter the message to encrypt: ").strip().encode()

    # Encrypt the message
    encrypted_message = fernet.encrypt(message)
    print("Encrypted Message (Cipher):", encrypted_message.decode())

if __name__ == "__main__":
    encrypt_message()

