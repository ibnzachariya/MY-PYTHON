# Caesar Cipher Program

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypt function
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter
    print(f"Encrypted text: {encrypted_text}")

# Decrypt function
def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            old_index = alphabet.index(letter)
            new_index = (old_index - shift_amount) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += letter
    print(f"Decrypted text: {decrypted_text}")

# Main program
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid choice. Please type 'encode' or 'decode'.")
