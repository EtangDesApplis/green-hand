from flask import Flask, request
from flask_cors import CORS
import os
from flask import send_from_directory
from pymongo import MongoClient
import pprint
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://%s/green-hand"%(os.getenv("DB_SERVICE"))
CORS(app)
#/gh-api/{userID}-{countertoken} GET request to verify user
mongo = PyMongo(app)


@app.route('/<path:tokenInfo>')
def verify(tokenInfo):
  #ID prendre la premiere valeur avant le trait
  id = int(tokenInfo.split('-')[0])
  print('id',id)
  countertoken = tokenInfo.split('-')[1]
  print('countertoken', countertoken)
  #IDuser
  user=mongo.db.users.find_one({"id":id})
  pprint.pprint(user)
  print(user["counter-token"])
  try:
    if countertoken == user["counter-token"]:
      mongo.db.users.update_one(
                {"id": id},
                {"$set": {"status":"verified"}}
            )
      return {"Status":"OK"}
    else :
      return {"Status":"KO"}
  except:
    print("Warning, unidentify requests")
    return {"Status":"KO"}



@app.route('/', methods=['POST'])
def post_route():

    #print(request.method)
    try:
      data = request.get_json()
      print("***********")
      print(data)
      print("***********")

      return {"Status":"OK"}
    except:
      return {"Status":"KO"}

if __name__=="__main__":
  #https://chefphan.com/gh-api/1-baa5a663ee0c22f57b3734ca
  #curl https://chefphan.com/gh-api/1-baa5a663ee0c22f57b3734ca
  #curl https://chefphan.com/gh-api/1-baa5a663ee0c22f57b3734ca/json
  #curl https://etangdesapplis.github.io/green-hand/
  #curl https://chefphan.com/gh-api/ -d "{"email":"nguyen.ensma@gmail.com","info":"","seeds":[{"variety":"rose","seedingOutdoor":["1"],"seedingIndoor":["1","3","6","9"],"harvest":["2"],"exposition":"","timeToHarvest":""}]}" -H 'Content-Type: application/json'
  #curl https://chefphan.com/gh-api/ -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  #to test with curl: curl localhost:5000 -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  #curl localhost:5000/Mandat.pdf

  app.run(host='0.0.0.0')