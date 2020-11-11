import smtplib
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep

class Scheduler:
    def __init__(self):
        self.users=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['users']
        self.seeds=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['seeds']
        self.events=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['events']
    
    def test(self):
        # generate fake events
        # events in form of JSON: {"label": "user-seed-YYYYMM", "email": "user@mail.com", "status": "todo"}
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
        #query users and seeds collections to generate events
        pass

    def run(self):
        while True:
            self.scheduleEvents()
            sleep(5)

if __name__=="__main__":
    daemon=Scheduler()
    daemon.test()
