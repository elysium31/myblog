from bcrypt import hashpw, gensalt, checkpw


def hash_password(password):
    return hashpw(password, gensalt())


def check_password(password, hashed):
    return checkpw(password, hashed)
