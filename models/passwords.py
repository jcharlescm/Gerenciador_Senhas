from datetime import datetime

class Password:

    def __init__(self, domain=None, usuario=None, password=None, expire=False):
        self.domain = domain
        self.user_str = usuario
        self.password = password
        self.create_at = datetime.now().isoformat()
        self.expire = 1 if expire else 0