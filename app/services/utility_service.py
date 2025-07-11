import bcrypt

def compare_passwords(password_1: str, password_2: str) -> bool:
    return bcrypt.checkpw(password_1.encode("utf-8"), password_2.encode("utf-8"))

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")