from flask import Flask , render_template , make_response , request , session

app = Flask(__name__)
app.config['SECRET_KEY'] = "2af888e0942c476c4eaeab2880a9e3d3a1426acb86730c1bd60b6d339f2256b2"

@app.route("/")
def index():
    print(session)
    if 'visits' not in session:
        session["visits"] = 1
    else:
        session["visits"] += 1
    return f"<h1>Посещения {session['visits']}</h1>"

data = [1,2,3,4]
@app.route("/numbs")
def numbs():
    if 'data' not in session: 
        session['data'] = data
        print(id(session['data']))
    else:
        session['data'][0] += 1
        session.modified = True

    return f"<h1>{session['data']}</h1>"


app.run(debug=True)



