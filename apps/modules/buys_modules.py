import datetime
from utils.valid_IDs import validando_id
class BuysModules:
    def __init__(self,id_user,id_product,qtt,price_at_buy,status,time = None,id_buy = None):
        self.id_buy = id_buy
        self.id_user = id_user
        self.id_product = id_product
        self.qtt = qtt
        self.price_at_buy = price_at_buy
        self.status = status
        self.time = time if time is not None else datetime.datetime.now()

    @property
    def id_buy(self):
        return self._id_buy
    @id_buy.setter
    def id_buy(self, NewID_buy):
        if NewID_buy is not None:
            validando_id(NewID_buy)
        self._id_buy = NewID_buy

    @property
    def id_user(self):
        return self._id_user
    @id_user.setter
    def id_user(self, NewID_user):
       if NewID_user is None:
           raise ValueError("O ID do usuário é obrigatório na compra.")
       self._id_user = validando_id(NewID_user)

    @property
    def id_product(self):
        return self._id_product
    @id_product.setter
    def id_product(self, NewID_product):
        if NewID_product is None:
            raise ValueError("O ID do produto é obrigatório na compra.")
        self._id_product = validando_id(NewID_product)

    @property
    def qtt(self):
        return self._qtt
    @qtt.setter
    def qtt(self, NewQtt):
        if not isinstance(NewQtt,int) or isinstance(NewQtt,bool):
            raise ValueError("A quantidade deve ser um número inteiro.")
        if NewQtt <= 0:
            raise ValueError("A quantidade não pode ser zero ou negativa.")
        self._qtt = NewQtt

    @property
    def price_at_buy(self):
        return self._price_at_buy
    @price_at_buy.setter
    def price_at_buy(self, NewPrice_at_buy):
        if not isinstance(NewPrice_at_buy,(int,float)) or isinstance(NewPrice_at_buy,bool):
            raise ValueError("O preço da compra deve ser um número.")
        if NewPrice_at_buy <= 0:
            raise ValueError("O preço da compra não pode ser zero ou negativo.")
        self._price_at_buy = NewPrice_at_buy

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, NewStatus):
        if hasattr(self, '_status') and self._status in ("completed", "canceled"):
            raise ValueError("A compra já foi finalizada ou cancelada e não pode mais ser alterada.")
        if not isinstance(NewStatus,str):
            raise ValueError("O status da compra deve ser uma string.")
        NewStatus = NewStatus.strip().lower()
        status_valid = ("processing","completed", "canceled")
        if NewStatus not in status_valid:
            raise ValueError("O status da compra deve ser 'processing', 'completed' ou 'canceled'.")
        self._status = NewStatus

   


