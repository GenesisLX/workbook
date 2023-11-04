# import sqlite3
# import tkinter

import os.path
import time
import bs4.element
from bs4 import BeautifulSoup
from selenium import webdriver
# from prettytable import PrettyTable
# from tasks_parsing import *
# from type_title_paring import *
import sys

# sys.path.insert(0, 'parsing/files')
# import parsing.parsing
# from parsing import parsing
# from db.db_work import *
from .parsing.parsing import *
from .db.db_work import *


# return_response()
# from parsing import *
# from work_db import *

DB_NAME = "test.db"
MAIN_SITE_URL = 'https://inf-oge.sdamgia.ru/'


def main(check=False):
    """Получение """
    if check:
        type_dict, title_dict, sub_title_dict = get_data_main_page(MAIN_SITE_URL)
        tasks_dict = get_data_page_of_tasks(title_dict, sub_title_dict)

        print(title_dict)
        print(sub_title_dict)
        print(tasks_dict)

        init_db(DB_NAME, type_dict, title_dict, sub_title_dict, tasks_dict)

    # 15 заданий не хватает
    # for i in range(1, 33):
    #     a = 0
    #     b = 0
    #     for key in tasks_dict:
    #         if tasks_dict[key][1] == i:
    #             a += 1
    #         if tasks_dict[key][2] == i:
    #             b += 1
    #     print(f'Количество заданий {i}:', a)
    #     print(f'Количество заданий {i}:', b)
    #     print("-" * 60)

    # for img in tasks_dict["body935672"][1].findAll("img"):
    #     img.attrs["src"] = "https://inf-oge.sdamgia.ru" + img.attrs["src"]
    # print(tasks_dict["body935672"][1])
    # get_css()


# def get_tasks():





if __name__ == "__main__":
    main()
