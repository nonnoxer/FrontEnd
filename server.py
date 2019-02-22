from flask import *
import sqlite3 as sqlite
app = Flask(__name__)

with sqlite.connect("database.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users(username, password);")

@app.route("/login",  methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with sqlite.connect("database.db") as conn:
            cur = conn.cursor()
            results = cur.execute("SELECT username FROM users WHERE username==? AND password==?;", (username,password)).fetchone()
        if results == None:
            return "Error invalid credentials"
        else:
            return "Hello " + results[0]
    else: #method is get
        return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with sqlite.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users VALUES (?,?);", (username, password))
            conn.commit()
        return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    with sqlite.connect("database.db") as conn:
        cur = conn.cursor()
        results = cur.execute("SELECT * FROM users;").fetchall()
    return str(results)

app.run(debug=True)
