from apps.modules.products_modules import ProductsModules, ProductGet, ProductUpdate
from apps.repository.products_repository import ProductRepository

class ProductService():
    def __init__(self):
        self.product_repository = ProductRepository()
    
    def create_product(self, name, qtt, expiration_date, price, img):
        product = ProductsModules(name, qtt, expiration_date, price, img)
        
        result = self.product_repository.create_product(product.name, product.qtt, product.expiration_date, product.price, product.img)
        
        return result
    
    def list_products(self):
        return self.product_repository.list_products()
    
    def get_product(self, id_product):
        verificacao = ProductGet(id_product)
        
        product = self.product_repository.get_product(verificacao.id_product)
        if product is None:
            raise ValueError("Produto não encontrado")
        
        return product
    
    def update_product(self, id_product, qtt, price, img):
        verificacao = ProductUpdate(id_product, qtt, price, img)
        self.product_repository.get_product(verificacao.id_product)
        
        result = self.product_repository.update_product(verificacao.id_product, verificacao.qtt, verificacao.price, verificacao.img)
        
        return result
    
    def delete_product(self, id_product):
        verificacao = ProductGet(id_product)
        self.product_repository.get_product(verificacao.id_product)
        
        result = self.product_repository.delete_product(verificacao.id_product)
        
        return result
    
    def update_stock(self, id_product, qtt):
        verificacao = ProductUpdate(id_product, qtt, None, None)
        self.product_repository.get_product(verificacao.id_product)
        
        result = self.product_repository.update_stock(verificacao.id_product, verificacao.qtt)
        
        return result
    
    def list_products_by_expiration(self):
        return self.product_repository.list_products_by_expiration()
    