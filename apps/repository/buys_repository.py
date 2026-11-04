from apps.database.conection import Conection
from psycopg.rows import dict_row

class BuysRepository:

    def create_buy(self,id_user,id_product,qtt,price_at_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                INSERT INTO buys(id_user,id_product,qtt,price_at_buy)
                VALUES (%s, %s, %s, %s)
                RETURNING id_buy, id_user, id_product, qtt, price_at_buy, status, time
                ''', (id_user,id_product,qtt,price_at_buy)
            )
            buy = cursor.fetchone()
            conn.commit()
            return buy

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def update_buy(self,id_buy,qtt,price_at_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                UPDATE buys
                SET qtt = %s, price_at_buy = %s
                WHERE id_buy = %s AND status = 'processing'
                RETURNING id_buy, id_user, id_product, qtt, price_at_buy, status, time
                ''', (qtt,price_at_buy,id_buy)
            )
            buy = cursor.fetchone()
            conn.commit()
            return buy

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def list_buys(self):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM buys
                ORDER BY id_buy DESC
                '''
            )
            buys = cursor.fetchall()
            return buys

        except Exception:
            conn.rollback()
            return []
        finally:
            cursor.close()
            conn.close()


    def get_buy(self,id_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM buys
                WHERE id_buy = %s
                ''', (id_buy,)
            )
            buy = cursor.fetchone()
            return buy

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def list_buy_by_user_id(self,id_user):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM buys
                WHERE id_user = %s
                ORDER BY id_buy DESC
                ''', (id_user,)
            )
            buys = cursor.fetchall()
            return buys

        except Exception:
            conn.rollback()
            return []
        finally:
            cursor.close()
            conn.close()


    def delete_buy(self,id_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                DELETE FROM buys
                WHERE id_buy = %s
                RETURNING id_buy, id_user, id_product, qtt, price_at_buy, status, time
                ''', (id_buy,)
            )
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            return 0
        finally:
            cursor.close()
            conn.close()


    def completed_buy(self,id_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                UPDATE buys
                SET status = 'completed'
                WHERE id_buy = %s AND status = 'processing'
                RETURNING id_buy, id_user, id_product, qtt, price_at_buy, status, time
                ''', (id_buy,)
            )
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            return 0
        finally:
            cursor.close()
            conn.close()


    def canceled_buy(self,id_buy):
        conn = Conection.connect()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                UPDATE buys
                SET status = 'canceled'
                WHERE id_buy = %s AND status = 'processing'
                RETURNING id_buy, id_user, id_product, qtt, price_at_buy, status, time
                ''', (id_buy,)
            )
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            return 0
        finally:
            cursor.close()
            conn.close()