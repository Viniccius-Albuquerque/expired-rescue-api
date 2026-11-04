from psycopg.rows import dict_row
from apps.database.conection import Conection

class ProductRepository():
    def create_product(name, qtt, expiration_date, price, img):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        INSERT INTO products (name, qtt, expiration_date, price, img)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id_product, name, qtt, expiration_date, price, img, created_at;
                        ''',
                        (name, qtt, expiration_date, price, img)
                    )
                    product = cursor.fetchone()
                    conn.commit()
                    return product
        except Exception:
            return None
            
    def list_products():
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        SELECT * FROM products;
                        '''
                    )
                    products = cursor.fetchall()
                    return products
        except Exception:
            return []
            
    def get_product(id_product):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        SELECT * FROM products WHERE id_product = %s;
                        ''',
                        (id_product,)
                    )
                    product = cursor.fetchone()
                    return product
        except Exception:
            return None
            
    def update_product(id_product, qtt, price, img):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        UPDATE products
                        SET qtt = %s, price = %s, img = %s
                        WHERE id_product = %s
                        RETURNING id_product, name, qtt, expiration_date, price, img, created_at;
                        ''',
                        (qtt, price, img, id_product)
                    )
                    product = cursor.fetchone()
                    conn.commit()
                    return product
        except Exception:
            return None
            
    def delete_product(id_product):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        DELETE FROM products WHERE id_product = %s
                        ''',
                        (id_product,)
                    )
                    conn.commit()
                    return cursor.rowcount
        except Exception:
            return 0
            
    def update_stock(id_product, new_qtt):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        UPDATE products
                        SET qtt = %s
                        WHERE id_product = %s
                        ''',
                        (new_qtt, id_product)
                    )
                    conn.commit()
                    return cursor.rowcount
        except Exception:
            return 0
            
    def list_product_by_expiration():
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        SELECT * FROM products
                        ORDER BY expiration_date ASC;
                        '''
                    )
                    products = cursor.fetchall()
                    return products
        except Exception:
            return []