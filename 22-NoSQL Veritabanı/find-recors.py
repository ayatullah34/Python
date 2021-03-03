import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

myclient = pymongo.MongoClient("mongodb+srv://ayatullahcan:3KEsnkTGL1XGHAkx@cluster0.joktn.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

result = mycollection.find_one()
print(result)

# for i in mycollection.find():
#     print(i)

# for i in mycollection.find({},{"_id":0,"name":1,"price":1}): #sonuç kısmında 1 yazanlar  görünür 0 yazanlar görünmez
#     print(i)

# for i in mycollection.find({},{"_id":0}):
#     print(i)

for i in mycollection.find({},{"name":1}):
    print(i)