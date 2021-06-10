import os
import psycopg2


class PostgresDB:

    @staticmethod
    def copy_db_from_csv(db_name):
        conn = psycopg2.connect(
            dbname=os.environ.get('DBNAME'),
            user=os.environ.get('USER'),
            host=os.environ.get('HOST'),
            port=os.environ.get('PORT'),
            options=os.environ.get('OPTIONS'),
            password=os.environ.get('PASSWORD')
        )
        cur = conn.cursor()
        with open('{}.csv'.format(db_name), newline='', encoding='utf-8') as file:
            next(file)
            cur.copy_from(file, '{}'.format(db_name), sep='|')
        conn.commit()
        cur.close()
        conn.close()





