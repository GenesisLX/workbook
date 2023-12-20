import sqlite3
# import SQLite_Core


def db_init_tables(db_name):
    con = sqlite3.connect(db_name)

    try:
        with con:
            cur = con.cursor()
            # Create tables

            con.execute("""CREATE TABLE IF NOT EXISTS answer_types (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NOT NULL
                        );""")

            con.execute("""CREATE TABLE IF NOT EXISTS themes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                answer_type_id INTEGER NOT NULL,
                name TEXT NOT NULL,                
                FOREIGN KEY(answer_type_id) REFERENCES answer_types(id));
                """)

            con.execute("""CREATE TABLE IF NOT EXISTS sub_themes(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL, 
             parent_Id INTEGER,
             deleted INTEGER NOT NULL DEFAULT 0,
             FOREIGN KEY(parent_Id) REFERENCES themes(id));""")

            con.execute("""CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sub_themes_id INTEGER,
                themes_id INTEGER,
                sourse_task_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                solution TEXT NOT NULL,
                verification_criteria TEXT,
                deleted INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY(sub_themes_id) REFERENCES sub_themes(id),
                FOREIGN KEY(themes_id) REFERENCES themes(id));
                """)

            con.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT UNIQUE NOT NULL
            )""")


    except Exception as ex:
        print(ex)

