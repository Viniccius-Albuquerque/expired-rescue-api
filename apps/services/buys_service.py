from apps.schemas.buys_schemas import BuyCreateSchema, BuyUpdateSchema
from apps.repository.buys_repository import BuysRepository
from apps.repository.products_repository import ProductRepository
from apps.repository.users_repository import UserRepository


class BuyService:
    def __init__(self, buy_repository, product_repository, user_repository):
        self.buy_repository = buy_repository
        self.product_repository = product_repository
        self.user_repository = user_repository


    def create_buy(self, id_user, id_product, qtt):
        user_existing = self.user_repository.get_user(id_user=id_user)
        if not user_existing:
            raise ValueError("Usuário não encontrado")
        product_existing = self.product_repository.get_product(id_product=id_product)
        if not product_existing:
            raise ValueError("Produto não encontrado")
        if product_existing["qtt"] < qtt:
            raise ValueError("Estoque insuficiente para a compra")
        price_at_buy = round(product_existing["price"] * qtt, 2)
        self.product_repository.update_stock(id_product, product_existing["qtt"] - qtt)

        return self.buy_repository.create_buy(
            id_user,
            id_product,
            qtt,
            price_at_buy
        )