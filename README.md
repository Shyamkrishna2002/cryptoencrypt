# cryptoencrypt
A beginner-friendly Python project for encrypting and decrypting messages using random key generation. This project demonstrates fundamental cryptographic concepts, error handling, and secure data encryption techniques.
# Features
- **Random Key Generation**: Automatically generates a secure, random 32-character key for encryption.
- **Encryption**: Encrypts a user-provided message and displays the cipher text along with the generated key.
- **Decryption**: Decrypts a cipher text using a user-provided key and checks for validity.
- **Error Handling**: Handles invalid keys and mismatched inputs, ensuring secure operations.

# How It Works

### **Encryption:**
- The script generates a random key.
- The user provides a message to encrypt.
- The key and encrypted message (cipher) are displayed.

### **Decryption:**
- The user inputs the previously generated key and cipher.
- The script validates the key and decrypts the message.
- If the key or cipher is incorrect, an error message is shown.

---

# Usage

### **Prerequisites:**
- Python 3.x
- Install the required library:
  pip install cryptography



# How to Run

### 1. **Encryption**
- Run the encryption script to generate a key and encrypt your message:
- python encrypt_message.py

### 2. **Decryption**
- python decrypt_message.py



# Code Examples

### **Encryption Example**

'''Enter the message to encrypt: Hello, World!
Generated Key (save this to decrypt): YWx0K2ZxM2N3bW5rb2QzNm5ldmpzMGFtZHNmMTU5NGM=
Encrypted Message (Cipher): gAAAAABhRNExr9eFuwDqN9JK3svzNBL6BVaIoGBy2UweHJeb4gg9FXaO1'''


### **Decryption Example**
  
-Enter the decryption key: YWx0K2ZxM2N3bW5rb2QzNm5ldmpzMGFtZHNmMTU5NGM=
-Enter the encrypted message (cipher): gAAAAABhRNExr9eFuwDqN9JK3svzNBL6BVaIoGBy2UweHJeb4gg9FXaO1
-Decrypted Message: Hello, World!



# Error Handling

- If the key or cipher text is incorrect, the program displays:
  ```plaintext
  Error: Decryption failed. The key or cipher text is incorrect.

  



   
