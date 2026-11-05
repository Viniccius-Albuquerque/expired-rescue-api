import datetime
from utils.valid_IDs import validando_id
from utils.valid_email import email as valid_email

class CodeModules:
    def __init__(self, id_code, value, time, id_user, email):
        self.id_code = id_code
        self.value = value
        self.time = time if time is not None else datetime.datetime.now()
        self.id_user = id_user
        self.email = email
        
    @property
    def id_code(self):
        return self.__id_code
    @id_code.setter
    def id_code(self, value):
        if value is not None:
            validando_id(value)
        self.__id_code = value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("value deve ser um número inteiro")
        if value < 1000 or value > 9999:
            raise ValueError("value deve ser um número inteiro de 4 dígitos")
        self.__value = value

    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, value):
        if value is not None:
            validando_id(value)
        self.__id_user = value
        
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        if value is not None:
            value = valid_email(value)
        self.__email = value    