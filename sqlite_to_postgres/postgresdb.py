import psycopg2


class PostgresDB:

    def __init__(self):
        pass

    @staticmethod
    def copy_db_from_csv(db_name):
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            host='localhost',
            port=5432,
            options=f'-c search_path=content',
            password='postgres'
        )
        cur = conn.cursor()
        with open('{}.csv'.format(db_name), newline='', encoding='utf-8') as file:
            next(file)
            cur.copy_from(file, '{}'.format(db_name), sep='|')
        conn.commit()
        cur.close()
        conn.close()
