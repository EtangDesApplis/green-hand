from flask import Flask, request
from flask_cors import CORS
import os
#from flask import send_from_directory
#from pymongo import MongoClient
import pprint
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://%s/green-hand"%(os.getenv("DB_SERVICE"))
CORS(app)
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def post_route():
    user=mongo.db.users.find_one({"id":1})
    pprint.pprint(user)
    return {"Status":"OK"}

if __name__=="__main__":
  #to test with curl: curl localhost:5000 -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  #curl localhost:5000/Mandat.pdf

  app.run(host='0.0.0.0')