# import init_db as db
from .db_core import db_execute, get_db_connection
from .init_db import db_init_tables
# import sqlite_core as sql_core
import sqlite3
from .sqlite_core import *
import os

DB_NAME = 'test.db'

def add_data_to_db(type_dict, title_dict, sub_title_dict, tasks_dict, con):
    add_type_in_db(con, type_dict)
    add_title_in_db(con, title_dict)
    add_sub_title_in_db(con, sub_title_dict)
    add_tasks_in_db(con, tasks_dict)


def init_db(DB_NAME, type_dict, title_dict, sub_title_dict, tasks_dict):
    # Todo: Изменить удаление БД на очищение таблиц в ней.
    if os.path.exists(f'back_end/db/{DB_NAME}'):
        drop_tables(["answer_types", "themes", "sub_themes", "tasks"], DB_NAME,
                    """DROP TABLE IF EXISTS """)
        # os.remove(f'back_end/db/{DB_NAME}')
    # db.db_init_tables(DB_NAME)
    db_init_tables(DB_NAME)
    con = db_connect(DB_NAME)
    try:
        with con:
            add_data_to_db(type_dict, title_dict, sub_title_dict, tasks_dict, con)

    except Exception as ex:
        print(ex)
#
# def select_user_by_login(login):
#     conn = get_db_connection(f'back_end/db/test.db')
#
#     with conn:
#         # conn.row_factory = sqlite3.Row
#         query = f"SELECT * FROM users WHERE login=?;"
#         item = db_execute(conn, query, (login,), True)
#         return item


def select_user_by_login(login):
    conn = db_connect(DB_NAME)
    cur = conn.cursor()
    with conn:
        # conn.row_factory = sqlite3.Row
        query = f"SELECT * FROM users WHERE login=?;"
        cur.execute(query, (login,))
        return cur.fetchone()


def reg_user(login, password):
    conn = db_connect(DB_NAME)
    cur = conn.cursor()
    with conn:
        query = "INSERT INTO users(login, password) VALUES(?, ?)"
        res = cur.execute(query, (login, password))
        conn.commit()
        # print(res.lastrowid)
        # print(cur.rowcount)


def get_titles(DB_NAME):
    con = db_connect(f"back_end/db/{DB_NAME}")
    try:
        with con:
            titles = select_titles(con)
            # print(titles)
            dict_titles = gen_dict_titles(titles, con)
            # print(titles)

            # print(sub_titles)
            # for sub_title in sub_titles:
            #     print(sub_title[0])
            #
            # for title in titles:
            #     print(title[0])

            return dict_titles
    except Exception as ex:
        print(ex)


def gen_dict_titles(titles, con):
    dict_titles = {}

    for el in titles:
        # print(el)
        sub_titles = select_sub_title(con, el)
        # print(sub_titles)
        dict_titles[el[2]] = el[0], sub_titles

    return dict_titles

    # except Exception as ex:
    #     print(ex)


def get_tasks(DB_NAME, val_tasks):
    # con = db_connect(f"back_end/db/{DB_NAME}")
    con = db_connect(DB_NAME)
    tasks_list = []
    try:
        with con:
            for i, val in enumerate(val_tasks):
                print(i + 1)
                print(val)
                if val != 0:
                    tasks_list.append(select_tasks(con, i + 1, val))
                # if val != 0:
            return tasks_list

    except Exception as ex:
        print(ex)
