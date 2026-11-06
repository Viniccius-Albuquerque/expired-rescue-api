from psycopg.rows import dict_row
from apps.database.conection import Conection

class CodeRepository:
    def create_code(value, time, id_user, email):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    cursor.execute(
                        '''
                        INSERT INTO codes (value, time, id_user, email)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id_code, value, time, id_user, email;
                        ''',
                        (value, time, id_user, email)
                    )
                    code = cursor.fetchone()
                    conn.commit()
                    return code
        except Exception:
            return None

    def delete_code(id_code):
        try:
            with Conection.connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        'DELETE FROM codes WHERE id_code = %s;',
                        (id_code,)
                    )
                    conn.commit()
                    return cursor.rowcount
        except Exception:
            return 0

    def valid_code(id_user, user_code, email):
        try:
            with Conection.connect() as conn:
                with conn.cursor(row_factory=dict_row) as cursor:
                    if id_user is None:
                        cursor.execute(
                            '''
                            SELECT id_code FROM codes 
                            WHERE id_user IS NULL 
                              AND value = %s 
                              AND email = %s 
                              AND time >= NOW();
                            ''',
                            (user_code, email)
                        )
                    else:
                        cursor.execute(
                            '''
                            SELECT id_code FROM codes 
                            WHERE id_user = %s 
                              AND value = %s 
                              AND email = %s 
                              AND time >= NOW();
                            ''',
                            (id_user, user_code, email)
                        )
                    
                    code = cursor.fetchone()
                    return 1 if code else 0
        except Exception:
            return 0