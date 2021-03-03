import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017")

myclient = pymongo.MongoClient("mongodb+srv://ayatullahcan:3KEsnkTGL1XGHAkx@cluster0.joktn.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]

mycollection = mydb["products"]

# product = {"name":"samsung s5","price":2000}
# result = mycollection.insert_one(product)

# print(result)
# print(result.inserted_id)

productList = [
    {"name":"Samsung S6", "price": 3000, "description":"iyi telefon"},
    {"name":"Samsung S7", "price": 4000, "categories": ['telefon','elektronik']}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)