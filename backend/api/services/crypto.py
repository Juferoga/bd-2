from cryptography.fernet import Fernet

clave = 'ZqZLgcBwJzrUbMUUuw5dAIBD48q_meDFPm-nX8UQJxU='
cifrado = Fernet(clave)

def encriptar(password : str):
    password_encoded = password.encode()
    return cifrado.encrypt(password_encoded).decode()

def desencriptar(password_encrypted : str):
    return cifrado.decrypt(password_encrypted).decode()