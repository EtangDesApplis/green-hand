from pymongo import MongoClient
from random import randint
import pprint
from secrets import token_hex

dictLanguage={0:"fr",1:"en",2:"es"}
dictExposition={0:"sunny",1:"shadow",2:"all"}

def printUsers(db):
    for doc in db["users"].find():
        pprint.pprint(doc)

def printSeeds(db):
    for doc in db["seeds"].find():
        pprint.pprint(doc)

def dataGen1(db,nbUser,nbSeedTypeMax):
    #two collections: user and seed
    userDB=db["users"]
    seedDB=db["seeds"]

    for i in range(nbUser):
        infoUser={
            "user-id": i+1,
            "email": "user%d@mail.com"%(i+1),
            "token": token_hex(6),
            "status": "unverified",
        }
        # pour in user info
        userDB.insert_one(infoUser)

        nbSeed=randint(1,nbSeedTypeMax)
        # one user can have multiple seeds to planify
        for j in range(nbSeed):
            month_ext=[randint(1,13),randint(1,13)]
            month_int=[randint(1,13),randint(1,13)]
            month_harvest=[randint(1,13),randint(1,13)]
            infoSeed={
                "user-id": i+1,
                "name":"seed%d"%(j),
                "ext-seeding":list(range(min(month_ext),max(month_ext))),
                "int-seeding":list(range(min(month_int),max(month_int))),
                "harvest": list(range(min(month_harvest),max(month_harvest))),
                "exposition": dictExposition[randint(0,2)],
                "language": dictLanguage[randint(0,2)],
            }
            # pour in seed info
            seedDB.insert_one(infoSeed)

if __name__=="__main__":
    client = MongoClient("myk3s.com",32017)
    db=client['green-hand']
    #generate data
    dataGen1(db,2,3)
    #print users database
    printUsers(db)
    #print seed database
    printSeeds(db)
    #test find_one
    ans=db["users"].find_one({"name":"noname"})
    print(ans)
    print(type(ans))