import datetime
import os
from utils.valid_IDs import validando_id
class products_modules:
    def __init__(self, id_product, name, qtt, expiration_date, price, img=None):
        self.id_product = id_product
        self.name = name
        self.qtt = qtt
        self.expiration_date = expiration_date
        self.price = price
        self.img = img

    @property
    def id_product(self):
        return self.__id_product
    @id_product.setter
    def id_product(self, id_product):
        if id_product is not None:
            validando_id(id_product)
        self.__id_product = id_product

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name deve ser uma string")
        value = value.strip()
        if len(value) < 4 or len(value) > 50:
            raise ValueError("name deve ter no mínimo 4 e no máximo 50 caracteres")
        if not any(char.isalnum() for char in value):
            raise ValueError("name não pode conter apenas caracteres especiais")
        self.__name = value

    @property
    def qtt(self):
        return self.__qtt
    @qtt.setter
    def qtt(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("qtt deve ser um número inteiro")
        if value < 0:
            raise ValueError("qtt deve ser um inteiro maior ou igual a zero")
        self.__qtt = value

    @property
    def expiration_date(self):
        return self.__expiration_date
    @expiration_date.setter
    def expiration_date(self, value):
        if not isinstance(value, datetime.date):
            raise TypeError("expiration_date deve ser um objeto datetime.date")
        if value <= datetime.date.today():
            raise ValueError("expiration_date deve ser estritamente no futuro (maior que a data atual)")
        self.__expiration_date = value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("price deve ser um número float")
        if value <= 0.0:
            raise ValueError("price deve ser estritamente maior que zero")
        self.__price = float(value)

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, value):
        if value is None:
            self.__img = None
            return
        if not isinstance(value, str):
            raise TypeError("img deve ser uma string com o caminho do arquivo")
        value = value.strip()
        if not value:
            self.__img = None
            return
        if len(value) > 255:
            raise ValueError("img não pode exceder 255 caracteres")
        extensoes_validas = ('.png', '.jpeg', '.jpg')
        if not value.lower().endswith(extensoes_validas):
            raise ValueError("img deve ter extensão válida (.png ou .jpeg)")
        if os.path.exists(value):
            if os.path.getsize(value) > 5 * 1024 * 1024:
                raise ValueError("img excede o tamanho limite de 5MB")
        self.__img = value
        
