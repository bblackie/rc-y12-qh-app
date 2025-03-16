from flask import Flask,g, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'cs_weapon.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    cursor = get_db().cursor()
    sql ="SELECT * FROM CS_Skins"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("contents.html", results=results)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        New_Weapon_id = request.form["Weapon_id"]
        New_Wear = request.form["Weapon_Wear"]
        New_Skin_Name = request.form["Skin_Name"]
        sql = "INSERT INTO CS_Skins(Weapon_id, Wear, Skin_Name) VALUES (?,?,?)"
        cursor.execute(sql,(New_Weapon_id,New_Wear,New_Skin_Name))
        get_db().commit()

    return redirect("/")
    
if __name__=="__main__":
    app.run(debug=True)
