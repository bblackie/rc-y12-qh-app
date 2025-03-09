from flask import Flask,g
import sqlite3
app = Flask(__name__)

@app.route("/")

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




def index():
    curser = get_db().curser()
    sql ='SELECT * FROM contents'
    curser.execute
    results = curser.fetchall()
    return str(results)
    
if __name__=="__main__":
    app.run(debug=True)
