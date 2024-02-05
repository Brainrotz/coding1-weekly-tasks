def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

# Example usage:
plaintext = input("Enter text: ")
shift_amount = int(input("Enter shift amount: "))

ciphered_text = caesar_cipher(plaintext, shift_amount)
print("Encrypted Text:", ciphered_text)