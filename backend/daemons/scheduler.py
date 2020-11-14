import smtplib
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep
"""
Project: Green Hands
Authors: nguyen.ensma@gmail.com
All rights reserved

Objectif: this daemon scan database of users and seeds and plan the notification in form of events and stored in database.
"""

class Scheduler:
    def __init__(self):
        self.users=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['users']
        self.seeds=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['seeds']
        self.events=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['events']
    
    def test(self):
        # generate fake events
        # events in form of JSON: {"label": "user-seed-YYYYMM-userID", "email": "user@mail.com", "status": "todo"}
        users=["elvire","cecile","quan"]
        emails=["elvire.meyers@gmail.com","wiart.ccil@gmail.com","nguyen.ensma@gmail.com"]
        currentTimeStamp=datetime.now().strftime("%Y%m")
        for i in range(5):
            for j in range(3):
                doc={"label":"%s-seed%d-%s"%(users[j],i,currentTimeStamp),
                     "email": "%s"%(emails[j]),
                     "status":"todo"
                }
                self.events.insert_one(doc)
                print("[INFO]: an event generated")
            sleep(300)
    
    def scheduleEvents(self):
        #if we are on 1st Jan of new year, change status of all users from planified to verified

        #query users and seeds collections to generate events
        for user in self.users.find({"status":"verified"}):
            for sid in user["seeds"]:
                seed=self.seeds.find_one({"id": sid})
                #event for outdoor activity
                for month in seed["ext"]:
                    timeStamp=int(datetime.now().strftime("%Y"))*100+int(month)
                    event={
                        "label":"%s-%s-%d-%d"%(user["name"],seed["name"],timeStamp,user["id"]),
                        "email": user["email"],
                        "status": "todo"
                    }
                    #create an event if not yet
                    if self.events.find_one({"label":event["label"]})==None:
                        self.events.insert_one(event)
            #change user status to planified ?
            self.users.update_one(
                                {"id": user["id"]},
                                {"$set": {"status":"planified"}}
                            )
            print("[INFO]: planified all events for user with id=%d"%(user["id"]))

    def run(self):
        while True:
            self.scheduleEvents()
            sleep(5)

if __name__=="__main__":
    daemon=Scheduler()
    #daemon.test() #dev only
    daemon.run()
