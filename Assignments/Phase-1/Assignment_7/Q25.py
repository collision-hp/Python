import re

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,}$'
    
    if re.match(pattern, password):
        return True
    else:
        return False

password = "StrongPass1!"
if validate_password(password):
    print("Password is secure.")
else:
    print("Password is not secure.")
