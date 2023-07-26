# Strong Password Detection

import re

# Dictionary of usernames and passwords
dicc = {
    "Marcus": "marcus123@abC",
    "Bob": "abc123@boB",
    "Lily": "okaysue@abC",
    "Elias": "okay123andabC",
    "Cristal": "okay123@abc",
    "Ana": "okay1@abC",
    "Stephany": "123456@!$123",
    "Linarez": "okay123@abC"
}


def strong_password_detection(username, password):
    """
    Checks if a password is strong based on various criteria.

    Args:
        username (str): The username.
        password (str): The password to be validated.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    # Check if the username is present in the password (case-insensitive)
    username_match = re.search(username.upper(), password.upper())

    # Check if the password contains at least one digit
    digit_match = re.search(r"\d", password)

    # Check for the presence of special characters (!, @, $, or _)
    special_char_match = re.search(r"[!@$_]", password)

    # Check for the presence of at least one lowercase and one uppercase letter
    lowercase_match = re.search(r"[a-z]", password)
    uppercase_match = re.search(r"[A-Z]", password)

    if len(password) < 10:
        print("Invalid password. It must be at least 10 characters long.")
        return False
    elif username_match is not None:
        print("Invalid password. The username cannot be part of the password.")
        return False
    elif digit_match is None:
        print("Invalid password. It must contain at least one digit.")
        return False
    elif special_char_match is None:
        print("Invalid password. It must contain at least one of the following special characters: !, @, $, _.")
        return False
    elif lowercase_match is None or uppercase_match is None:
        print("Invalid password. It must contain at least one lowercase and one uppercase letter.")
        return False
    else:
        print("Congratulations! You have chosen a strong password. Keep it safe and don't forget it.")
        return True


# Main code
print("Password Validation Results:")
print("----------------------------")
# Iterate over the dictionary and check each user's password
for username, password in dicc.items():
    print("Username:", username)
    print("Password:", password)
    print("Result:", strong_password_detection(username, password))
    print("----------------------------------------")
