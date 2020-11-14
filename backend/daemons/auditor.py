"""
Project: Green Hands
Authors: nguyen.ensma@gmail.com
All rights reserved

Objectif: this daemon verifies identity of user to avoid spam email by saboters
"""

import smtplib
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep, time
from secrets import token_hex

class Auditor:
    def __init__(self):
        self.login=os.getenv("LOGIN")
        self.password=os.getenv("PASSWORD")
        self.users=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['users']
        self.seeds=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['seeds']
    
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
                "scheduled":[],
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
                "ext":[1,2,3,4,5,6,7,8,9,10,11,12],
                "name": "seed%d"%(i)
            }
            self.seeds.insert_one(seed)
            print("[INFO]: added new seed")

    def requestVerification(self):
        #need to optimize number of login /close
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(self.login,self.password)
            #query for unverified users
            for user in self.users.find({"status":"unverified"}):
                #send email with tokens and verification url
                url="https://chefphan.com/gh-api/%s-%s"%(user["id"],user["counter-token"])
                data="From: %s\nTo: %s\nSubject: %s\nHi %s,\nWelcome to Green Hands community !\nPlease keep safely your Auth token: %s\n Please click on this URL to verify your email:\n %s"%(self.login,user["email"],"Email verification",user["name"],user["token"],url)
                server.sendmail(self.login,user["email"],data)
                #update status to pending
                self.users.update_one(
                                {"id": user["id"]},
                                {"$set": {"status":"pending", "timeStamp":time()}}
                            )
                print("[INFO]: sent verification email to a new user")
            server.close()
        except:
            print("[ERROR]: issue with email server")

    def cleanUp(self):
        #query for pending users
        now=time()
        for user in self.users.find({"status":"pending"}):
            #if timeout remove users & seed linked to this users (spam info)
            if (now-user["timeStamp"] > 259200.): #3 days in seconds
                #delete all linked seeds
                for id in user["seeds"]:
                    self.seeds.delete_one({"id": id})
                    print("[INFO]: deleted a seed from timeouted unverified user")
                #delete user
                self.users.delete_one({"id": user["id"]})
                print("[INFO]: deleted a timeouted unverified user")

    def run(self):
        while True:
            self.requestVerification()
            self.cleanUp()
            sleep(60)

if __name__=="__main__":
    daemon=Auditor()
    daemon.test() #dev only
    daemon.run()
        

        

