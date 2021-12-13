import flask
import json
from flask import jsonify,request
import datetime
from pymongo import MongoClient
con = MongoClient()
db = con.Class
post = db.Classdata
app = flask.Flask(__name__)
app.config["DEBUG"] = True
def getdictkey(mydict,value):
    return [k for k, v in mydict.items() if v ==value]
with open('data.json') as f:
    data = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return jsonify(data)
@app.route('/findWally', methods=['GET'])
def data_all():
    for i in range(len(data['News'])):
        A = data['News'][i]
        if(A['Detail']['Author']=='Wally'):
            return jsonify(A)

@app.route('/createNews', methods=['GET'])
def mangodb():
    df = data['News']
    for i in range(0,len(df)):
        db.post.insertOne({title:A["Title"],author:A["Details"]["Author"],date:A["Date"]})
        
@app.route('/findNews', methods=['GET'])
    df = data["News"]
    for i in range(0,len(df)):
        db.user.ensureIndex({A["Title"]:1,A["Details"]["Author"]:1})
app.run()

