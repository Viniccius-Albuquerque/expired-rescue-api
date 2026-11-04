from apps.database.conection import Conection
from psycopg.rows import dict_row

class UserRepository:
    
    def register_user(self, name, password, email):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                INSERT INTO users(name, password, email)
                VALUES (%s, %s, %s)
                RETURNING id_user, name, email, type, adress, img, created_at
                ''', (name, password, email)
            )
            user = cursor.fetchone()
            conn.commit()
            return user

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def list_users(self):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM users
                ORDER BY id_user DESC
                '''
            )
            users = cursor.fetchall()
            return users

        except Exception:
            conn.rollback()
            return []
        finally:
            cursor.close()
            conn.close()


    def get_user_by_email(self,email):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM users
                WHERE email = %s
                ''', (email,)
            )
            user = cursor.fetchone()
            return user

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def get_user(self,id_user):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                SELECT * FROM users
                WHERE id_user = %s
                ''', (id_user,)
            )
            user = cursor.fetchone()
            return user

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def delete_user(self,id_user):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                DELETE FROM users
                WHERE id_user = %s
                RETURNING id_user, name, email, type, adress, img, created_at
                ''', (id_user,)
            )
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            return 0
        finally:
            cursor.close()
            conn.close()


    def update_user(self,id_user, name, email, adress, img):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                UPDATE users
                SET name = %s, email = %s, adress = %s, img = %s
                WHERE id_user = %s
                RETURNING id_user, name, email, type, adress, img, created_at
                ''', (name, email, adress, img, id_user)
            )
            user = cursor.fetchone()
            conn.commit()
            return user

        except Exception:
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()


    def update_password(self,id_user,password,new_password):
        conn = Conection.conectar()
        cursor = conn.cursor(row_factory=dict_row)
        try:
            cursor.execute(
                '''
                UPDATE users
                SET password = %s
                WHERE id_user = %s 
                RETURNING id_user, name, email, type, adress, img, created_at
                ''', (new_password, id_user)
            )
            conn.commit()
            return cursor.rowcount

        except Exception:
            conn.rollback()
            return 0
        finally:
            cursor.close()
            conn.close()