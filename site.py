from flask import Flask , render_template , make_response , request , session
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "13ff826b791d380d38992bba4aa0ca5f6be6c910c4ad429b1c6b7c69eceed30c"
app.permanent_session_lifetime = datetime.timedelta(days=10)

@app.route("/")
def index():
    print(session)
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return f"<h1>Посещения</h1>{session['visits']}"

data = [1,2,3,4]
@app.route("/numbs")
def numbs():
    session.permanent = True
    if 'data' not in session:
        session['data'] = data
    else :
        session['data'][1] += 1
        session.modified = True

        
    return f"<h1>Числа</h1>{session['data']}"

app.run(debug = True)


