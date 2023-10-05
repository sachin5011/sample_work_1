from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def passwordencriptor(password):
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    
    return hashed_password

def decryptpassword(hashed_password, password):
    valid = bcrypt.check_password_hash(hashed_password, password)
    return valid


     

