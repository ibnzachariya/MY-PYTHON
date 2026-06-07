import random
import string


def generate_custom_password():
    # Get user inputs
    num_letters = int(input("Enter the number of letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_special = int(input("Enter the number of special characters: "))

    # Create pools of characters
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Pick random characters from each pool
    password_chars = []
    password_chars += random.choices(letters, k=num_letters)
    password_chars += random.choices(digits, k=num_digits)
    password_chars += random.choices(special_chars, k=num_special)

    # Shuffle to mix characters
    random.shuffle(password_chars)

    # Join to form the password string
    password = ''.join(password_chars)
    return password


# Generate and print the password
print("Generated password:", generate_custom_password())
