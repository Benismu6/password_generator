import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generates a random password based on specified constraints.

    Args:
        length (int): The length of the password. Defaults to 16.
        nums (int): The minimum number of digits in the password. Defaults to 1.
        special_chars (int): The minimum number of special characters in the password. Defaults to 1.
        uppercase (int): The minimum number of uppercase letters in the password. Defaults to 1.
        lowercase (int): The minimum number of lowercase letters in the password. Defaults to 1.

    Returns:
        str: The generated password.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # Define constraints
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
# Generate a new password with default constraints
new_password = generate_password()
print('Generated password:', new_password)
