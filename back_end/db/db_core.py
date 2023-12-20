import sqlite3


def get_db_connection(db_name):
    return sqlite3.connect(db_name)


def db_execute(db_connection, query, params=None, return_res=False):
    cur = db_connection.cursor()
    try:
        if params is None:
            cur.execute(query)
        else:
            cur.execute(query, params)
            # db_connection.commit()
        if return_res:
            # return cur.fetchall()
            return cur.fetchone()
        db_connection.commit()
    except Exception as e:
        print(e)
