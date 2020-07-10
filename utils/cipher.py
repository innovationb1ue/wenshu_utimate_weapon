from datetime import datetime

from utils.decode_components import des3encrypt
from utils.token import RequestVerificationToken


class CipherText(str):
    def __new__(cls):
        return cls.cipher()

    @classmethod
    def cipher(cls) -> str:
        date = datetime.now()
        timestamp = str(int(date.timestamp() * 1000))
        salt = RequestVerificationToken(24)
        iv = date.strftime("%Y%m%d")

        enc = des3encrypt(plain_text=timestamp, key=salt, iv=iv)
        cipher_text = cls.str2binary(salt + iv + enc)

        return super(CipherText, cls).__new__(cls, cipher_text)

    @staticmethod
    def str2binary(string: str) -> str:
        return " ".join(bin(ord(item))[2:] for item in string)
