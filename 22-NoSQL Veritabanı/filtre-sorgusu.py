import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

myclient = pymongo.MongoClient("mongodb+srv://ayatullahcan:3KEsnkTGL1XGHAkx@cluster0.joktn.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

filter = {"name":"samsung s5"}

# result = mycollection.find(filter)
# result = mycollection.find_one(filter)
# result = mycollection.find_one({"_id":ObjectId("5f9d6935f9d9f6d8c52ce8ca")})

# print(result)

# result = mycollection.find({
#     "name": {
#         "$in" : ["samsung s5,Samsung S6"]
#     }
# })

""" 
result = mycollection.find({
    "price": {
        "$gt" : 200 # gt --greater than,gte büyük ve eşit
    }
}) 
"""

""" 
result = mycollection.find({
    "price": {
        "$eq" : 200 # eq --eşit
    }
})
 """


""" 
result = mycollection.find({
    "price": {
        "$lt" : 200 # lt -- 2000 den küçük lte küçük ve eşit 
    }
})
 """

result = mycollection.find({
    "name": {
        "$regex" : "^S" # adı s ile başlayanlar
    }
})

for i in result:
    print(i)
