import sqlite3
import random


def db_connect(db_name):
    return sqlite3.connect(db_name)


# def exec_query(conn, query, return_res=False, return_res_many=False):
#     cur = conn.cursor()
#     try:
#         cur.execute(query)
#
#         if return_res:
#             return cur.fetchone()
#         if return_res_many:
#             return cur.fetchall()
#         conn.commit()
#
#     except Exception as ex:
#         print(ex)


def exec_query(conn, query, first=False):
    cur = conn.cursor()
    try:
        cur.execute(query)
        if first:
            return cur.fetchone()
        return cur.fetchall()
    except Exception as ex:
        print(ex)

def exec_command(conn, query):
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

def drop_tables(table_names, db_name, query):
    conn = db_connect(db_name)
    for table_name in table_names:
        # exec_query(conn, query + table_name)
        exec_command(conn, query + table_name)





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



def select_titles(conn):
    with conn:
        # conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # cur.execute(f"""SELECT t.id, t.name, st.name
        # from themes t join sub_themes st on st.parent_Id = t.id""")
        #
        # titles = cur.fetchall()

        # print(test)
        # for el in test:
        #     for i in el:
        #         print(i)
        #
        #     print(el)

        cur.execute(f"""SELECT * FROM themes WHERE answer_type_id != 3""")
        titles = cur.fetchall()


        return titles


def select_sub_title(conn, title):
    with conn:

        cur = conn.cursor()
        cur.execute(f"""SELECT name FROM sub_themes WHERE sub_themes.parent_Id = {title[0]}""")
        sub_titles = cur.fetchall()
        return sub_titles

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



def select_tasks(conn, themes_id, val_tasks):
    cur = conn.cursor()
    # t.sourse_task_id, t.content, t.solution, t.verification_criteria

    non_sort_task_list = exec_query(conn, f"""SELECT t.content, t.solution, t.verification_criteria, th.answer_type_id
                         FROM themes th
                              join sub_themes st on th.id  = st.parent_Id 
                              join tasks t on st.id = t.sub_themes_id 
                         WHERE th.id={themes_id}""")

    print(non_sort_task_list)
    print("----------------------")
    return random.choices(non_sort_task_list, k=val_tasks)
    # a = exec_query(conn, f"""SELECT * FROM tasks WHERE sub_themes_id = {task_type}""")
    # b = exec_query(conn, f"""SELECT * FROM tasks WHERE themes_id = {task_type}""")
    #
    # if a is None:
    #     sample_b = random.sample(b, task_num)
    #     return sample_b
    # else:
    #     sample_a = random.sample(a, task_num)
    #     return sample_a




def test():
    con = db_connect(f"back_end/db/test.db")
    # a = exec_query(con, "SELECT * FROM tasks WHERE id=15", return_res_many=True)
    a = exec_query(con, "SELECT * FROM tasks WHERE id=15")
    print(a)














