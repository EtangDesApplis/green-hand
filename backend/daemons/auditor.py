"""
Project: Green Hands
Authors: nguyen.ensma@gmail.com
All rights reserved

Objectif: this daemon verifies identity of user to avoid spam email by saboters
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep, time
from secrets import token_hex

def getTimeStamp():
  return datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")

def printERROR(data):
  print(getTimeStamp()+"[ERROR] "+data)

def printINFO(data):
  print(getTimeStamp()+"[INFO] "+data)

def printWARN(data):
  print(getTimeStamp()+"[WARN] "+data)

class Auditor:
    def __init__(self):
        self.login=os.getenv("LOGIN")
        self.password=os.getenv("PASSWORD")
        self.users=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['users']
        self.seeds=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['seeds']
        self.env=Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),"templates")),trim_blocks=True)
    
    def test(self):
        #inject fake user & fake seed
        users=["Elvire","Cecile","Quan"]
        emails=["elvire.meyers@gmail.com","wiart.ccil@gmail.com","nguyen.ensma@gmail.com"]
        for i in range(len(users)):
            user={
                "name": users[i],
                "id": i,
                "email":emails[i],
                "status":"unverified",
                "seeds":[i],
                "token": token_hex(6),
                "counter-token": token_hex(12),
                "timeStamp": time()
            }
            # add user
            self.users.insert_one(user)
            print("[INFO]: added new user")
            seed={
                "id": i,
                "seedingOutdoor":[4,5,6,7,8,9,10],
                "seedingIndoor":[1,2,3,11,12],
                "variety": "seed%d"%(i)
            }
            self.seeds.insert_one(seed)
            print("[INFO]: added new seed")

    def requestVerification(self):  
        #query for unverified users
        unverifiedUsers=self.users.find({"status":"unverified"})
        if unverifiedUsers != None:
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.ehlo()
                server.login(self.login,self.password)
                for user in unverifiedUsers:
                    #send email with tokens and verification url
                    url="https://chefphan.com/gh-api/%d-%s"%(user["id"],user["counter-token"])

                    msg=MIMEMultipart('alternative')
                    msg['Subject']="Email verification"
                    msg['From']=self.login
                    msg['To']=user["email"]
                    data=MIMEText(self.env.get_template('emailVerification.html').render(user="Quan",token=user["token"], link=url),'html')
                    msg.attach(data)
                    server.sendmail(self.login,user["email"],msg.as_string())

                    #update status to pending
                    self.users.update_one(
                                    {"id": user["id"]},
                                    {"$set": {"status":"pending", "timeStamp":time()}}
                                )
                    printINFO("sent verification email to user with id = %d"%(user["id"]))
                server.close()
            except:
                printERROR("issue with email server")

    def cleanUp(self):
        #query for pending users
        now=time()
        for user in self.users.find({"status":"pending"}):
            #if timeout remove users & seed linked to this users (spam info)
            if (now-user["timeStamp"] > 259200.): #3 days in seconds
                #delete all linked seeds
                for id in user["seeds"]:
                    self.seeds.delete_one({"id": id})
                    printWARN("deleted a seed from timeouted unverified user, seed id = %d"%(id))
                #delete user
                self.users.delete_one({"id": user["id"]})
                printWARN("deleted a timeouted unverified user, id = %d"%(user["id"]))

    def run(self):
        while True:
            self.requestVerification()
            self.cleanUp()
            sleep(60)

if __name__=="__main__":
    daemon=Auditor()
    daemon.test() #dev only
    daemon.run()
        

        

