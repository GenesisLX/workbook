# import flask

# from flask import render_template, flash, redirect, session, url_for, request, g
from flask import *

from back_end.db.db_work import get_titles
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask.ext.login import login_user, logout_user, current_user, login_required
# from db import *
from UserLogin import UserLogin

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"

# @app.route('/')
# def hello():
#     return "<p>Hello</p>"

@app.route("/tasks")
def tasks():
    list = [{1: ["str1", "ans1", "crit1"]}, {2: ["str2", "ans2", "crit2"]}]
    for i in list:
        for key in i:
            print(i[key][0])

    return render_template("task.html", list=list)


@app.route('/test', methods=['GET', 'POST'])
def task_choice():
    list_sub_titles, list_titles = get_titles("test.db")
    return render_template("list.html", list_sub_titles=list_sub_titles, list_titles=list_titles)




@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return redirect("tasks")
        # return test()
    else:
        return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return redirect("tasks")
        # return test()
    else:
        return render_template('login.html', title='Sign in')

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

