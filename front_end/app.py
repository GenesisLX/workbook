# import flask

# from flask import render_template, flash, redirect, session, url_for, request, g
from flask import *
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from back_end.db.db_work import get_titles, reg_user, get_tasks, select_user_by_login
from back_end.work_with_back import main
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask.ext.login import login_user, logout_user, current_user, login_required
# from db import *
from UserLogin import UserLogin

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
# login_manager.login_message_category = "success"

# @app.route('/')
# def hello():
#     return "<p>Hello</p>"

def print_cont():
    return "<p>Привет!</p>"

class User():
    def __init__(self, login):
        self.login = login

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.login)



@app.route("/tasks", methods=['GET', 'POST'])
@login_required
def tasks(val_tasks):
    print(val_tasks)
    list_problem = get_tasks("test.db", val_tasks)
    # print(list_problem)
    # for el in list_problem:
    #     for i in el:
    #         print(i[2])



    # list = [("str1", "ans1", "crit1"), ("str2", "ans2", "crit2")]
        # for i in list:
        #     for key in i:
        #         print(i[key][0])

    return render_template("task.html", list=list_problem)


@app.route("/menu", methods=['GET', 'POST'])
@login_required
def menu():
    dict = get_titles("test.db")
    if request.method == 'POST':
        val_tasks = []
        for i in range(1, len(dict)+1):
            val_tasks.append(int(request.form["input_value"+str(i)]))

        for val in val_tasks:
            if val != 0:
                break
        else:
            return render_template("menu.html", dict=dict)



        # b = request.form["input_value"]
        # print(val_tasks)
        return tasks(val_tasks)
    else:
        return render_template("menu.html", dict=dict)




@app.route('/test', methods=['GET', 'POST'])
@login_required
def task_choice():
    list_sub_titles, list_titles = get_titles("test.db")
    return render_template("list.html", list_sub_titles=list_sub_titles, list_titles=list_titles)



@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']

        if len(user_name) > 3:
            user = select_user_by_login(user_name)
            if user is not None:
                flash("Такой пользователь уже существует!", "error")
            if len(password) > 4:
                reg_user(user_name, password)
                login_user(User(user_name))
                return redirect(url_for("menu"))
            else:
                flash("Слишком короткий пароль!", "error")
        else:
            flash("Слишком короткое имя!", "error")


    return render_template('registration.html')




@login_manager.user_loader
def load_user(user_id):
    user = select_user_by_login(user_id)
    if user is None:
        return None
    return User(user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        user = select_user_by_login(user_name)

        if user is not None and user[2] == password:
            login_user(User(user_name))
            return redirect(url_for("menu"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/update_db")
@login_required
def update_db():
    main(True)
    return redirect(url_for("menu"))



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('profile'))
#
#     if request.method == 'POST':
#         login = request.form['Login']
#         password = request.form['Password']
#         print(login)
#         user = get_user_by_login(login)
#
#         if user == None:
#             return render_template('authorization.html', title='Sign in')
#         else:
#             try:
#                 if user[2] == password:
#                     return redirect("tasks")
#             except Exception as ex:
#                 print(ex)
#
#     else:
#         # return render_template('login.html', title='Sign in')
#         return render_template('authorization.html', title='Sign in')

# @app.route("/tasks")
# def hello(name):
#     return f"Hello, {escape(name)}!"


# @app.route("/test")
# def hello(name):
#     con = db_connect(DB_NAME)
#     with con:
#         print(None)





@app.route("/")
@login_required
def hub():
    if request.method == 'POST':
        event = request.form
    else:
        return render_template("main.html")




def run():
    app.run()
    get_titles("test.db")







# if __name__ == "__main__":
#     app.run()

