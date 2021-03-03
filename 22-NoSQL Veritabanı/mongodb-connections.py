import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

myclient = pymongo.MongoClient("mongodb+srv://ayatullahcan:3KEsnkTGL1XGHAkx@cluster0.joktn.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

print(myclient.list_database_names())