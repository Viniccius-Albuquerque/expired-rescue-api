from apps.schemas.buys_schemas import BuyCreateSchema, BuyUpdateSchema
from apps.repository.buys_repository import BuysRepository
from apps.repository.products_repository import ProductRepository
from apps.repository.users_repository import UserRepository


class BuyService:
    def __init__(self,buy_repository: BuysRepository,product_repository: ProductRepository,user_repository: UserRepository):

        self.buy_repository = buy_repository
        self.product_repository = product_repository
        self.user_repository = user_repository


    def create_buy(self, id_user, id_product, qtt):
        buys_create = BuyCreateSchema(id_product=id_product, qtt=qtt)
        user_existing = self.user_repository.get_user(id_user=id_user)
        if not user_existing:
            raise ValueError("Usuário não encontrado")
        product_existing = self.product_repository.get_product(id_product=buys_create.id_product)
        if not product_existing:
            raise ValueError("Produto não encontrado")
        if product_existing["qtt"] < buys_create.qtt:
            raise ValueError("Estoque insuficiente para a compra")
        price_at_buy = round(product_existing["price"] * buys_create.qtt, 2)
        self.product_repository.update_stock(
            buys_create.id_product,
            product_existing["qtt"] - buys_create.qtt
        )
        return self.buy_repository.create_buy(
            id_user,
            buys_create.id_product,
            buys_create.qtt,
            price_at_buy
        ) 

    def update_buy(self, id_buy, qtt):
        buy_update = BuyUpdateSchema(qtt=qtt)
        buy_existing = self.buy_repository.get_buy(id_buy=id_buy)
        if not buy_existing:
            raise ValueError("Compra não encontrada")
        if buy_existing["status"] != "processing":
            raise ValueError("Só é possível alterar compras em processamento.")
        product = self.product_repository.get_product(id_product=buy_existing["id_product"])
        if not product:
            raise ValueError("Produto não encontrado")
        diff_qtt = buy_update.qtt - buy_existing["qtt"]
        if diff_qtt > 0 and product["qtt"] < diff_qtt:
            raise ValueError("Estoque insuficiente para atualizar a compra")
        new_stock = product["qtt"] - diff_qtt
        self.product_repository.update_stock(buy_existing["id_product"], new_stock)
        new_price = round(product["price"] * buy_update.qtt, 2)
        return self.buy_repository.update_buy(id_buy, buy_update.qtt, new_price)


    def completed_buy(self, id_buy):
        buy_existing = self.buy_repository.get_buy(id_buy=id_buy)
        if not buy_existing:
            raise ValueError("Compra não encontrada")
        if buy_existing["status"] != "processing":
            raise ValueError("Apenas compras em processamento podem ser concluídas")
        return self.buy_repository.completed_buy(id_buy)


    def canceled_buy(self, id_buy):
        buy_existing = self.buy_repository.get_buy(id_buy=id_buy)
        if not buy_existing:
            raise ValueError("Compra não encontrada")
        if buy_existing["status"] != "processing":
            raise ValueError("Apenas compras em processamento podem ser canceladas")
        product = self.product_repository.get_product(id_product=buy_existing["id_product"])
        if product:
            self.product_repository.update_stock(
                buy_existing["id_product"],
                product["qtt"] + buy_existing["qtt"]
            )
        return self.buy_repository.canceled_buy(id_buy)


    def list_buys(self):
        return self.buy_repository.list_buys()


    def get_buy(self, id_buy):
        buy = self.buy_repository.get_buy(id_buy)
        if not buy:
            raise ValueError("Compra não encontrada")
        return buy


    def list_buy_by_user_id(self, id_user):
        return self.buy_repository.list_buy_by_user_id(id_user)


    def delete_buy(self, id_buy):
        buy = self.buy_repository.get_buy(id_buy)
        if not buy:
            raise ValueError("Compra não encontrada")
        return self.buy_repository.delete_buy(id_buy)