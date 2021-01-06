from flask import Flask, request
from flask_cors import CORS
import os
#from flask import send_from_directory
#from pymongo import MongoClient
import pprint
from flask_pymongo import PyMongo
from secrets import token_hex
from time import time
from datetime import datetime

def getTimeStamp():
  return datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")

def printERROR(data):
  print(getTimeStamp()+"[ERROR] "+data)

def printINFO(data):
  print(getTimeStamp()+"[INFO] "+data)

def printWARN(data):
  print(getTimeStamp()+"[WARN] "+data)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://%s/green-hand"%(os.getenv("DB_SERVICE"))
CORS(app)
#/gh-api/{userID}-{countertoken} GET request to verify user
mongo = PyMongo(app)


@app.route('/<path:tokenInfo>')
def verify(tokenInfo):
  #ID prendre la premiere valeur avant le trait
  id = int(tokenInfo.split('-')[0])
  #print('id',id)
  countertoken = tokenInfo.split('-')[1]
  #print('countertoken', countertoken)
  #IDuser
  user=mongo.db.users.find_one({"id":id})
  #pprint.pprint(user)
  #print(user["counter-token"])
  try:
    if countertoken == user["counter-token"]:
      mongo.db.users.update_one(
                {"id": id},
                {"$set": {"status":"verified"}}
            )
      printINFO("verified user with id = %d"%(id))
      return {"Status":"OK"}
    else :
      printERROR("failed to verify user with id = %d"%(id))
      return {"Status":"KO"}
  except:
    printWARN("unidentified request")
    return {"Status":"KO"}



@app.route('/', methods=['POST'])
def post_route():
  
  #try:
    data = request.get_json()
    # check if user is registered
    if mongo.db.users.find_one({"email":data["email"]})==None:
      # unknown user
      # get max id
      status=mongo.db.status.find_one()
      if status==None:
        # first run ever
        uid=0
        sid=0
        uNb=0
        sNb=0
        #create status
        mongo.db.status.insert_one({"uMID":-1,"uNb":0,"sMID":-1,"sNb":0})
      else:
        uid=status["uMID"]+1
        sid=status["sMID"]+1
        uNb=status["uNb"]
        sNb=status["sNb"]

      # add seed info here
      seedList=[]
      for item in data["seeds"]:
        seed={
                "id": sid,
                "seedingOutdoor":item["seedingOutdoor"],
                "seedingIndoor":item["seedingIndoor"],
                "variety": item["variety"],
                "harvest": item["harvest"],
                "exposition": item["exposition"],
                "timeToHarvest": item["timeToHarvest"]
            }
        mongo.db.seeds.insert_one(seed)
        seedList.append(sid)
        sid=sid+1

      # add user
      user={
            "name": data["name"],
            "id": uid,
            "email":data["email"],
            "status":"unverified",
            "info": data["info"],
            "seeds":seedList,
            "token": token_hex(4),
            "counter-token": token_hex(12),
            "timeStamp": time()
            }

      mongo.db.users.insert_one(user)

      #update status
      mongo.db.status.update_one({},{"$set":{"uMID":uid,"uNb":uNb+1,"sMID":sid,"sNb":sNb+len(seedList)}})
      printINFO("added new user with id = %d"%(uid))
      return {"Status":"OK"}
    else:
      # reject for the moment due to lack of auth
      printWARN("registried user failed to update with email = %s"%(data["email"]))
      return {"Status":"email already used"}
    
    
@app.route('/login', methods=['POST'])
def login_route():
  
  #try:
    data = request.get_json()
    userInfo=mongo.db.users.find_one({"token":data["token"]})
    if userInfo==None:
      # unknown user
      printWARN("registried user failed to authenticate with token = %s"%(data["token"]))
      return {"Status":"unknown user"}
    else:
      print (type(userInfo))
      return str(userInfo)

    
    
@app.route('/add', methods=['POST'])
def add_route(): 
    data = request.get_json()
    # check if user is registered
    userInfo=mongo.db.users.find_one({"token":data["token"]})
    if userInfo==None:
      # unknown user
      printWARN("registried user failed to authenticate with token = %s"%(data["token"]))
      return {"Status":"unknown user"}
    else:
      # add seed info here
      status=mongo.db.status.find_one()
      sid=status["sMID"]
      seedList=userInfo["seeds"]
      for item in data["seeds"]:
        #check if seed doesnt exists in the database already
        if mongo.db.seeds.find_one({"variety":item["variety"]})==None:
          seed={
                  "id": sid,
                  "seedingOutdoor":item["seedingOutdoor"],
                  "seedingIndoor":item["seedingIndoor"],
                  "variety": item["variety"],
                  "harvest": item["harvest"],
                  "exposition": item["exposition"],
                  "timeToHarvest": item["timeToHarvest"]
              }
          mongo.db.seeds.insert_one(seed)
          seedList.append(sid)
          sid=sid+1
      #update status 
      mongo.db.users.update_one({"token":data["token"]},{"$set":{"seeds":seedList}})
      printINFO("updated user with id = %d"%(userInfo["id"]))
      return {"Status":"OK"}
    
@app.route('/delete', methods=['POST'])
def delete_route():
    data = request.get_json()
    userInfo=mongo.db.users.find_one({"token":data["token"]})
    
    print(userInfo)
    if userInfo==None:
      # unknown user
      printWARN("registried user failed to authenticate with token = %s"%(data["token"]))
      return {"Status":"unknown user"}
    else:
      uid=userInfo["id"]
      # update seed info here
      seedList=userInfo["seeds"]
      for item in data["seeds"]:
        seedVariety=mongo.db.seeds.find_one({"variety":item["variety"]})
        seedList.remove(seedVariety["id"])
      #update status
      mongo.db.users.update_one({"token":data["token"]},{"$set":{"seeds":seedList}})
      printINFO("updated user with id = %d"%(uid))
      return {"Status":"OK"}

    

if __name__=="__main__":
  
  app.run(host='0.0.0.0')
