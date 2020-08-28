from flask import Flask, Response, jsonify
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)

conn="sqlite:///my_db.sqlite"

engine = create_engine(conn, pool_recycle=3600)

@app.route("/")
def index():
    return "<h1>Deployed!</h1>"


@app.route("/longitude")
def longitude():
    response = pd.read_sql("SELECT * FROM earthquake2 LIMIT 10", engine)
    istype=type(response)
    return istype

@app.route("/latitude")
def psqltest():
    #response = pd.read_sql("SELECT * FROM longitude LIMIT 10", engine)
    #result= jsonify(response)
    result="latitude"
    return result

if __name__ == "__main__":
    app.run()