import pymongo
import datetime

client = pymongo.MongoClient()
db = client.test
testcollection = db.testcollection
print(db.collection_names(include_system_collections=False))
print(testcollection.find_one({"name":"jack"}))
new_posts = [{"author": "Mike",
"text": "Another post!",
"tags": ["bulk", "insert"],
"date": datetime.datetime(2009, 11, 12, 11, 14)},
{"author": "Eliot",
"title": "MongoDB is fun",
"text": "and pretty easy too!",
"date": datetime.datetime(2009, 11, 10, 10, 45)}]
testcollection.insert_many(new_posts)
print(testcollection.find_one({"author":"Mike"}))

