from flask import Flask, request
from flask_cors import CORS
import os
from flask import send_from_directory
from pymongo import MongoClient
import pprint
from flask_pymongo import PyMongo
from secrets import token_hex


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
  try:
    #step 1 validate email
    # separer le json en deux parties
    #rajouter l'id dans le json pour le test
    # questionner la base de donné pour l'id
    # questionner la base de donné pour l'email

    data = request.get_json()

    #print("***********")
    print(data)
    #print("***********")

    # check if user is registered
    if mongo.db.users.find_one({"email":data["email"]})==None:
      # unknown user
      # get max id
      status=mongo.db.status.find_one()
      if status==None:
        # first run ever
        uid=0
        #create status
        mongo.db.status.insert_one({"uMID":0,"uNb":1})
      else:
        uid=status["uMID"]+1
        #update status
        mongo.db.status.update_one({},{"$set":{"uMID":status["uMID"]+1,"uNb":status["uNb"]+1}})

      # add seed info here
      user={
            "name": data["name"],
            "id": uid,
            "email":data["email"],
            "status":"unverified",
            "seeds":[],
            "token": token_hex(6),
            "counter-token": token_hex(12),
            "timeStamp": time()
            }
      mongo.db.users.insert_one(user)
      return {"Status":"OK"}
    else:
      # reject for the moment due to lack of auth
      return {"Status":"email already used"}
  except:
    return {"Status":"KO"}

if __name__=="__main__":
  #https://chefphan.com/gh-api/1-baa5a663ee0c22f57b3734ca
  #curl https://chefphan.com/gh-api/ -d '{"email":"nguyen.ensma1@gmail.com","username":"Quan","info":"","seeds":[{"variety":"rose","seedingOutdoor":["3"],"seedingIndoor":["4"],"harvest":["6"],"exposition":"","timeToHarvest":"50"}]}' -H 'Content-Type: application/json'

  app.run(host='0.0.0.0')