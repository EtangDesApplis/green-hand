import smtplib
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep

class Reminder:
    def __init__(self):
        self.login=os.getenv("LOGIN")#"greenhands.noreply@gmail.com"
        self.password=os.getenv("PASSWORD")#"9reenHand$"
        self.collection=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['events']
        #self.collection=MongoClient("myk3s.com",32017)['green-hand']['events']
    
    def test(self,email,subject,content):
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(self.login,self.password)
            data="From: %s\nTo: %s\nSubject: %s\n%s"%(self.login,email,subject,content)
            print(data)
            server.sendmail(self.login,email,data)
            server.close()
        except:
            print("Something went wrong...")

    def queryEvents(self):
        #get time stamp in format of YYYYMM
        currentTimeStamp=datetime.now().strftime("%Y%m")
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(self.login,self.password)
            # events in form of JSON: {"label": "user-seed-YYYYMM", "email": "user@mail.com", "status": "todo"}
            events=self.collection.find()
            for event in events:
                try:
                    if event["status"]=="todo":
                        tmp=event["label"].split('-')
                        if tmp[2]==currentTimeStamp:
                            data="From: %s\nTo: %s\nSubject: %s\nJust a kind reminder to plant your %s"%(self.login,event["email"],"Reminder from green hands",tmp[1])
                            server.sendmail(self.login,event["email"],data)
                            print("[INFO]: sending notifications")
                            #mark as done
                            self.collection.update_one(
                                {"label": event["label"]},
                                {"$set": {"status":"done"}}
                            )
                except:
                    print("[WARNING]: Event DB is not consistent")
            server.close()
        except:
            print("[ERROR]: issue with email server")

    def run(self):
        while True:
            self.queryEvents()
            sleep(5)


if __name__=="__main__":
    daemon=Reminder()
    #daemon.test("nguyen.ensma@gmail.com","test email", "Hello thee")
    daemon.run()