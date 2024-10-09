import re

def validate_password(password):
    #check if password has at least 8 characters
    if len(password) < 8:
        return False
    
    #check if password has at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    #check if password has at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    #check if password has at least one digit
    if not re.search(r'\d', password):
        return False
    
    #check if password has at least one special char
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    #if all conditions met, passwrd valid
    return True

password = input("Input your password: ")
is_valid = validate_password(password)

if is_valid:
    print("Valid Password")
else:
    print("Password does not meet requiremnts: needs to have at least one uppercase, lowercase, digit, special character, and has to be longer than 8 characters")