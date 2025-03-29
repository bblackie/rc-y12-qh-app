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
    sql ="""
select Catigory_Wepons.weapon_name, weapon_name, CS_Skins.Wear,
CS_Skins.Skin_Name, CS_Skins.Price
from CS_Skins
join Catigory_Wepons
on CS_Skins.Weapon_id = Catigory_Wepons.id
"""
    cursor.execute(sql)
    results = cursor.fetchall()

    cur = get_db().cursor()
    sql = "select * FROM catigory_Wepons" 
    cur.execute("SELECT id, weapon_name FROM Catigory_Wepons")
    catigory_Wepons = cur.fetchall()


    return render_template("contents.html", results=results, catigory_Wepons=catigory_Wepons)

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        Weapon_id = request.form["Weapon_id"]
        Wear = request.form["Weapon_Wear"]
        Skin_Name = request.form["Skin_Name"]
        price = request.form["Price"]
        sql = "INSERT INTO CS_Skins(Weapon_id, Wear, Skin_Name, Price) VALUES (?,?,?,?)"
        cursor.execute(sql,(Weapon_id,Wear,Skin_Name,price))
        get_db().commit()
    return redirect("/")

@app.route('/delete', methods=["GET","POST"])
def delete():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["Weapon_id"])
        sql = "DELETE FROM CS_Skins WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect("/")


        
if __name__=="__main__":
    app.run(debug=True)