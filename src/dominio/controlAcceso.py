import hashlib
import os
 
 
class ControlAcceso:
    _ITERACIONES = 100_000
 
    @staticmethod
    def cifrar_contraseña(contraseña: str) -> str:
        salt = os.urandom(16)
        hash_bytes = hashlib.pbkdf2_hmac('sha256', contraseña.encode('utf-8'), salt,
                                          ControlAcceso._ITERACIONES)
        return f"{salt.hex()}:{hash_bytes.hex()}"
 
    @staticmethod
    def validar_credenciales(usuario, contraseña_ingresada: str) -> bool:
        if not usuario.contraseña or ":" not in usuario.contraseña:
            return False
        salt_hex, hash_hex = usuario.contraseña.split(":", 1)
        salt = bytes.fromhex(salt_hex)
        hash_esperado = bytes.fromhex(hash_hex)
        hash_intento = hashlib.pbkdf2_hmac('sha256', contraseña_ingresada.encode('utf-8'),
                                            salt, ControlAcceso._ITERACIONES)
        return hash_intento == hash_esperado