import bcrypt
from utils.valid_email import email as valid_email
from utils.valid_IDs import validando_id

class UserModules:
    def __init__(self,name,password,email,type,adress,img,id_user = None):
        self.id_user = id_user
        self.name = name
        self.password = password
        self.email = email
        self.type = type
        self.adress = adress
        self.img = img

    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, NewID_user):
        if NewID_user is not None:
            validando_id(NewID_user)
        self._id_user = NewID_user

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,NewName):
        if not isinstance(NewName,str):
            raise TypeError("O nome do usuário deve ser uma string.")
        NewName = NewName.strip()
        if not NewName:
            raise ValueError("O nome do usuário não pode ser vazio.")
        if len(NewName) < 4 or len(NewName) > 50:
            raise ValueError("O nome do usuário deve ter entre 4 e 50 caracteres.")
        if not NewName.replace(" ", "").isalpha():
            raise ValueError("O nome não pode conter números ou caracteres especiais.")
        self._name = NewName

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,NewPassword):
        if not isinstance(NewPassword,str):
            raise TypeError("A senha do usuário deve ser uma string.")
        NewPassword = NewPassword.strip()
        if not NewPassword:
            raise ValueError("A senha do usuário não pode ser vazia.")
        if len(NewPassword) < 6 or len(NewPassword) > 15:
            raise ValueError("A senha do usuário deve ter entre 6 e 15 caracteres.")

        password_bytes = NewPassword.encode('utf-8')
        salt = bcrypt.gensalt()
        hash_gerado = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
        self._password = hash_gerado

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,NewEmail):
        self._email = NewEmail
        
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self,NewType):
        if not isinstance(NewType,str):
            raise TypeError("O tipo do usuário deve ser uma string.")
        NewType = NewType.strip().lower()
        types_valid = ("client","finance", "admin")
        if NewType not in types_valid:
            raise ValueError("O tipo do usuário deve ser 'client', 'finance' ou 'admin'.")
        self._type = NewType

    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self,NewAdress):
        if self.type == "client":
            if not isinstance(NewAdress,str) or not NewAdress.strip():
               raise TypeError("O endereço é obrigatorio para clientes.")
        if NewAdress is not None:
            NewAdress = str(NewAdress).strip()
        self._adress = NewAdress

    @property
    def img(self):
        return self._img
    @img.setter
    def img(self,NewImg):
        if NewImg is not None:
            NewImg = NewImg.strip()
            extencion_valid = (".jpg",".jpeg",".png")
            if not NewImg.lower().endswith(extencion_valid):
                raise ValueError("A imagem do usuário deve ter extensão .jpg, .jpeg ou .png.")
        self._img = NewImg