import datetime

class code_modules:
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
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("id deve ser um número inteiro")
            if value <= 0:
                raise ValueError("id deve ser maior que zero")
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
        if value is None:
            self.__id_user = None
        else:
            self.__id_user = value
            