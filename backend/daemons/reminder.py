"""
Project: Green Hands
Authors: nguyen.ensma@gmail.com
All rights reserved

Objectif: this daemon looks for events and sends respective notification to user when the time comes 
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from pymongo import MongoClient
from datetime import datetime
import os
from time import sleep

def getTimeStamp():
  return datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")

def printERROR(data):
  print(getTimeStamp()+"[ERROR] "+data)

def printINFO(data):
  print(getTimeStamp()+"[INFO] "+data)

def printWARN(data):
  print(getTimeStamp()+"[WARN] "+data)

class Reminder:
    def __init__(self):
        self.login=os.getenv("LOGIN")
        self.password=os.getenv("PASSWORD")
        self.events=MongoClient(os.getenv("DB_SERVICE"))['green-hand']['events']
        #self.events=MongoClient("myk3s.com",32017)['green-hand']['events']
        self.env=Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),"templates")),trim_blocks=True)
    
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

    def test2(self,email,subject,content):
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(self.login,self.password)

            msg=MIMEMultipart('alternative')
            msg['Subject']=subject
            msg['From']=self.login
            msg['To']=email
            data=MIMEText(self.env.get_template('indoorSeedling.html').render(user="Quan",seed="rose"),'html')
            msg.attach(data)

            server.sendmail(self.login,email,msg.as_string())
            server.close()
        except:
            print("Something went wrong...")

    def queryEvents(self):
        #get time stamp in format of YYYYMM
        currentTimeStamp=datetime.now().strftime("%Y%m")
        # events in form of JSON: {"label": "user-seed-YYYYMM-uid-type", "email": "user@mail.com", "status": "todo", "timeStamp":"YYYYMM"}
        events=self.events.find({"status":"todo","timeStamp":currentTimeStamp})
        if len(events)>0:
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.ehlo()
                server.login(self.login,self.password)
                for event in events:
                    if event["status"]=="todo":
                        tmp=event["label"].split('-')
                        msg=MIMEMultipart('alternative')
                        msg['Subject']="Reminder from green hands"
                        msg['From']=self.login
                        msg['To']=event["email"]
                        if tmp[4]=="int":
                            data=MIMEText(self.env.get_template('indoorSeedling.html').render(user=tmp[0],seed=tmp[1]),'html')
                        else:
                            data=MIMEText(self.env.get_template('outdoorSeedling.html').render(user=tmp[0],seed=tmp[1]),'html')
                        msg.attach(data)
                        server.sendmail(self.login,event["email"],msg.as_string())
                        printINFO("sending notifications to user with id = %s"%(tmp[3]))
                        #mark as done
                        self.events.update_one(
                            {"label": event["label"]},
                            {"$set": {"status":"done"}}
                        )
                server.close()
            except:
                printERROR("issue with email server")

    def run(self):
        while True:
            self.queryEvents()
            sleep(5)


if __name__=="__main__":
    daemon=Reminder()
    #daemon.test("nguyen.ensma@gmail.com","test email", "Hello thee")
    #daemon.test2("nguyen.ensma@gmail.com","test email", "Hello thee")
    daemon.run()