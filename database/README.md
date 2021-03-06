# green-hand

## Database architecture

![Architecture of Database](../resources/green-hands-DB.png)

## Template of JSON to push to Database
Client UI should be designed to capture these fields
```
{
  "user-id": 1
  "name": "concombre gynial",
  "ext-seeding": [3,4,5,6],
  "int-seeding": [3,4],
  "harvest": [7,8,9,10],
  "exposition": [],
  "language": "fr"
}
```

User data should be stored in database too
```
{
    "user-id": 1,
    "email": "user@mail.com",
    "token": 2341,
    "status": "unverified"
}
```
## Basic mongodb commands

For full reference: https://docs.mongodb.com/manual/crud/

```
show dbs;
use green-hand;
show collections;
db.users.find()
db.users.updateOne({"name":"Quan"},{$set: {"status":"verified"}})
```

## Test API

```
curl https://chefphan.com/gh-api/ -d \
'{"email":"nguyen.ensma@gmail.com","username":"Quan","info":"","seeds":[{"variety":"rose","seedingOutdoor":["3"],"seedingIndoor":["4"],"harvest":["6"],"exposition":"","timeToHarvest":"50"}]}' \
-H 'Content-Type: application/json'
```