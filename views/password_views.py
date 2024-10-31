import string, secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
from typing import Union


class FernetHasher:
    # Todos os caracteres Minúsculos e Maiúculos
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    # É a pasta real onde eu quero salvar
    KEY_DIR = BASE_DIR / 'keys'    

    def __init__(self, key: Union[Path, str]):
        if not isinstance(key, bytes):
            key = key.encode()
        self.fernet = Fernet(key)

    # print("string TEste de programa")
    @classmethod
    def _get_random_string(cls, lenght=5):
        string = ''
        for i in range(lenght):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)
            # print(string)
        # print(string)    
        return string


    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.archive_key(key)
        # Se não existir retorna o arquivo vazio
        return key, None


    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        # Verifica se o arquivo key.key existe
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(5)}.keys'

        with open(cls.KEY_DIR / file, 'wb') as arq:
            arq.write(key)

        # Retorna o caminho do arquivo que tem a chave
        return cls.KEY_DIR / file        


    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode('utf-8')
        return self.fernet.encrypt(value)


    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode('utf-8')
        
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token inválido'


