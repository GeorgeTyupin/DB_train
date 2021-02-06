import sqlite3
from flask import Flask , render_template , make_response , request , session , redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "2af888e0942c476c4eaeab2880a9e3d3a1426acb86730c1bd60b6d339f2256b2"


@app.route("/" , methods = ['GET' , 'POST'])
def index():
    if request.method == 'GET':
        if 'auth' in session and session['auth']:
            return f"<h1>Привет {session['login']}"
        else:
            return render_template('auth.html')
    else:
        mail = request.form.get('login')
        password = request.form.get('pass')

        with sqlite3.connect("computer_shop.db") as cur:
            sql = f"SELECT * FROM Users WHERE Mail = '{mail}' "
            print(sql)
            result = cur.execute(sql).fetchone()
            if (result and result[3] == password):

                session['login'] = result[1]
                session['id'] = result[0]
                session['color'] = result[4]
                session['auth'] = True

                response = make_response(redirect(f"/main"))
                return response
            else:
                return render_template('auth.html')
        return "123"

@app.route("/reg" ,  methods = ['GET' , 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('reg.html')

    if request.method == 'POST':
        mail = request.form.get('mail')
        with sqlite3.connect("computer_shop.db") as cur:
            sql = f"SELECT * FROM Users WHERE Mail = '{mail}'"
            print(sql)
            result = cur.execute(sql).fetchone()

        if result:
            return "Такой пользователь уже существует"

        login = request.form.get('login')
        password = request.form.get('password')
        color = request.form.get('color')

        with sqlite3.connect("computer_shop.db") as cur:
            sql = f"""INSERT INTO Users ('Mail' , 'Login' , 'Password' , 'color') 
            VALUES ('{mail}','{login}','{password}','{color}')"""
            cur.execute(sql)
            cur.commit()

        with sqlite3.connect("computer_shop.db") as cur:
            sql = f"SELECT ID FROM Users WHERE Mail = '{mail}'"
            result = cur.execute(sql).fetchone()
        
        session['login'] = login
        session['id'] = result[0]
        session['color'] = color
        session['auth'] = True

        response = make_response(redirect(f"/main"))
        return response

@app.route("/main" ,  methods = ['GET' , 'POST'])
def main():
    if request.method == 'GET':
        with sqlite3.connect("computer_shop.db") as cur:
            sql = "SELECT LOGIN FROM Users"
            result = cur.execute(sql).fetchall()
        users_login = []
        for i in result:
            users_login.append(i[0])

        return render_template('main.html' , data = session , users = users_login)

app.run(debug=True)
