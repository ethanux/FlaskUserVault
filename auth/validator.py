import re

def validate_name(name):
    """
    Validate a name.

    Parameters:
    - name (str): The name to validate.

    Returns:
    - bool: True if the name is valid, False otherwise.
    """
    # Regular expression to match only alphabets and spaces
    pattern = "^[A-Za-z ]+$"
    
    # Check if the name matches the pattern
    if re.match(pattern, name):
        if len(name) > 3 :
            return True
    else:
        return False

def validate_email(email):
    """
    Validate an email address.

    Parameters:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email address is valid, False otherwise.
    """
    # Regular expression for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_password(password, retype):
    """
    Validate a password and its retype.

    Parameters:
    - password (str): The password to validate.
    - retype (str): The retyped password to validate.

    Returns:
    - bool: True if both passwords are valid and match, False otherwise.
    """
    # Check if passwords are not empty and match
    if password and retype and password == retype:
        # Check if password meets criteria (e.g., length, complexity)
        if len(password) >= 8:  # Adjust as per your requirements
            return True
        else:
            print("Password should be at least 8 characters long.")
            return False
    else:
        print("Passwords do not match.")
        return False

