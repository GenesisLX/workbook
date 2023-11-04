# import init_db as db
from .init_db import db_init_tables
# import sqlite_core as sql_core
import sqlite3
from .sqlite_core import *
import os



def add_data_to_db(type_dict, title_dict, sub_title_dict, tasks_dict, con):
    add_type_in_db(con, type_dict)
    add_title_in_db(con, title_dict)
    add_sub_title_in_db(con, sub_title_dict)
    add_tasks_in_db(con, tasks_dict)


def init_db(DB_NAME, type_dict, title_dict, sub_title_dict, tasks_dict):
    #Todo: Изменить удаление БД на очищение таблиц в ней.
    if os.path.exists(f'back_end/db/{DB_NAME}'):
        os.remove(f'back_end/db/{DB_NAME}')
    # db.db_init_tables(DB_NAME)
    db_init_tables(f"back_end/db/{DB_NAME}")
    con = db_connect(f"back_end/db/{DB_NAME}")
    try:
        with con:
            add_data_to_db(type_dict, title_dict, sub_title_dict, tasks_dict, con)

    except Exception as ex:
        print(ex)


def get_titles(DB_NAME):
    con = db_connect(f"back_end/db/{DB_NAME}")
    try:
        with con:
            sub_titles, titles = select_title(con)
            print(sub_titles)
            print(titles)
            return sub_titles, titles
    except Exception as ex:
        print(ex)





    # except Exception as ex:
    #     print(ex)





