"""
Caesar Cipher Encryption & Decryption Tool
SkillCraft Technology - Cyber Security Internship - Task 01
"""


def encrypt(text, shift):
    """Encrypts the given text using Caesar Cipher with the given shift."""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave numbers, spaces, punctuation unchanged
            result += char
    return result


def decrypt(text, shift):
    """Decrypts the given text using Caesar Cipher with the given shift."""
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)


def main():
    print("=" * 50)
    print("       CAESAR CIPHER - ENCRYPT / DECRYPT TOOL")
    print("=" * 50)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (e.g. 3): "))
            except ValueError:
                print("Invalid shift value. Please enter a whole number.")
                continue
            encrypted = encrypt(message, shift)
            print(f"\nEncrypted message: {encrypted}")

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value used originally: "))
            except ValueError:
                print("Invalid shift value. Please enter a whole number.")
                continue
            decrypted = decrypt(message, shift)
            print(f"\nDecrypted message: {decrypted}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
