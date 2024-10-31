import string, secrets

class FernetHasher:
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_lowercase

    @classmethod
    def _get_random_string(cls, lenght=25):
        string = ''
        for i in range(lenght):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)
    
        return string


