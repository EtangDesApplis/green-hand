from flask import Flask, request
from flask_cors import CORS
import os
from flask import send_from_directory
from pymongo import MongoClient


users = MongoClient(os.getenv("DB_SERVICE"))['green-hand']['users']
seeds = MongoClient(os.getenv("DB_SERVICE"))['green-hand']['seeds']


app = Flask(__name__)
CORS(app)
#/gh-api/{userID}-{countertoken} GET request to verify user

@app.route('/<path:tokenInfo>')
def verify(tokenInfo):
  #ID prendre la premiere valeur avant le trait
  id = tokenInfo.split('-')[0]
  countertoken = tokenInfo.split('-')[1]
  #IDuser
  user=users.find_one({"id":id})
  try:
    if countertoken == user["counter-token"]:
      users.update_one(
                {"id": id},
                {"$set": {"status":"verified"}}
            )
  except:
    print("Warning, unidentify requests")


@app.route('/', methods=['POST'])
def post_route():

    #print(request.method)
    try:
      data = request.get_json()
      print(data)

      return {"Status":"OK"}
    except:
      return {"Status":"KO"}

if __name__=="__main__":
  #to test with curl: curl localhost:5000 -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  #curl localhost:5000/Mandat.pdf

  app.run(host='0.0.0.0')