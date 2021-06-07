import pymongo
from pymongo import MongoClient
import dns
client = pymongo.MongoClient("mongodb+srv://embee:<password>@embeedelicouscluster.iv9rq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["EmbeesData"]
collection = db["names"]



#post = {"_id":0,"name":"mcdee","age":23}
#collection.insert_one(post)

result = collection.find({})
for i in result:
    print(i["name"])