import sqlite3
import random


def db_connect(db_name):
    return sqlite3.connect(db_name)


def exec_query(conn, query):
    cur = conn.cursor()
    try:
        cur.execute(query)
        conn.commit()
    except Exception as ex:
        print(ex)


# # add type - Done
# con.execute("""INSERT INTO answer_types(id, name) VALUES(?, ?), (type_dict[key], key)""")
#
# #add title - Done
# con.execute("""INSERT INTO themes VALUES(?, ?, ?), (title_dict[key][0], title_dict[key][1], title_dict[key])""")
#
#
# #add sub_title
# con.execute("""INSERT INTO sub_themes VALUES(?, ?, ?, ?), (sub_title_dict[key][0], sub_title_dict[key][2], sub_title_dict[key][1], 0)""")
#
# #add tasks - Done
# # key = id в словаре, id на сайте, отношение к под-теме, отношение к теме, content, solve, ver_crit.
# con.execute("""INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?, ?, ?), (key, tasks_dict[key][1], tasks_dict[key][2], tasks_dict[key][0], tasks_dict[key][3], tasks_dict[key][4], tasks_dict[key][5], 0)""")


def add_type_in_db(conn, type_dict):
    type_list = []
    for key in type_dict:
        type_list.append((type_dict[key], str(key)))
    print(type_list)

    with conn:
        conn.executemany("INSERT INTO answer_types VALUES(?, ?)", type_list)
        # for key in type_dict:
        #     exec_query(conn, f"""INSERT INTO answer_types(id, name) VALUES(?, ?), ({type_dict[key]}, '''{key}''')""")


def add_title_in_db(conn, title_dict):
    title_list = []
    for key in title_dict:
        title_list.append((title_dict[key][0], title_dict[key][1], str(key)))
    print(title_list)

    with conn:
        conn.executemany("INSERT INTO themes VALUES(?, ?, ?)", title_list)


        # for key in title_dict:
        #     exec_query(conn, f"""INSERT INTO themes VALUES(?, ?, ?), ({title_dict[key][0]}, {title_dict[key][1]}, '''{key}'''))""")


def add_sub_title_in_db(conn, sub_title_dict):
    sub_title_list = []
    for key in sub_title_dict:
        sub_title_list.append((sub_title_dict[key][0], str(sub_title_dict[key][2]), sub_title_dict[key][1], 0))
    print(sub_title_list)

    with conn:
        conn.executemany("INSERT INTO sub_themes VALUES(?, ?, ?, ?)", sub_title_list)
        # for key in sub_title_dict:
        #     exec_query(conn, f"""INSERT INTO sub_themes VALUES(?, ?, ?, ?), ({sub_title_dict[key][0]}, '''{sub_title_dict[key][2]}''', {sub_title_dict[key][1]}, 0)""")


def add_tasks_in_db(conn, tasks_dict):
    tasks_list = []
    for key in tasks_dict:
        tasks_list.append((key, tasks_dict[key][1], tasks_dict[key][2], str(tasks_dict[key][0]), str(tasks_dict[key][3]), str(tasks_dict[key][4]), str(tasks_dict[key][5]), 0))

    print(tasks_list)

    with conn:
        conn.executemany("INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?, ?, ?)", tasks_list)

        # for key in tasks_dict:
        #     exec_query(conn, f"""INSERT INTO tasks VALUES(?, ?, ?, ?, ?, ?, ?, ?), ({key}, {tasks_dict[key][1]}, {tasks_dict[key][2]}, '''{tasks_dict[key][0]}''', '''{tasks_dict[key][3]}''', '''{tasks_dict[key][4]}''', '''{tasks_dict[key][5]}''', 0)""")



def select_title(conn):
    with conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM themes""")
        titles = cur.fetchall()
        cur.execute(f"""SELECT * FROM sub_themes""")
        sub_titles = cur.fetchall()


        return sub_titles, titles


    # cur = conn.cursor()
    # try:
    #     cur.execute(f"""SELECT * FROM sub_themes""")
    #     sub_titles = cur.fetchall()
    #     cur.execute(f"""SELECT * FROM themes""")
    #
    #     titles = cur.fetchall()
    #     conn.commit()
    #
    #     return sub_titles, titles
    # except Exception as ex:
    #     print(ex)


    # return titles



def select_tasks(conn, task_type, task_num):
    a = exec_query(conn, f"""SELECT * FROM tasks WHERE sub_themes_id = {task_type}""")
    b = exec_query(conn, f"""SELECT * FROM tasks WHERE themes_id = {task_type}""")

    if a is None:
        sample_b = random.sample(b, task_num)
        return sample_b
    else:
        sample_a = random.sample(a, task_num)
        return sample_a

















