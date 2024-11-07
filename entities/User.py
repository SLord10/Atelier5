class User:
    def __init__(self, nom, login, password):
        self._nom = nom
        self._login = login
        self._password = password

    def __repr__(self):
        return self._nom
    
    def getPassword(self):
        return self._password