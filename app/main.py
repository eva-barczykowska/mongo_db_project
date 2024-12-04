import os
from pymongo import MongoClient

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# Connect to the database and collection
db = client.my_database
collection = db.my_collection

# Insert a document
records = [{"name": "Alice", "age": 25, "city": "New York"},
           {"name": "Bob", "age": 30, "city": "London"},
           {"name": "Charlie", "age": 28, "city": "Paris"},
           {"name": "David", "age": 32, "city": "Tokyo"},
           {"name": "Eve", "age": 27, "city": "Berlin"},
           {"name": "Frank", "age": 35, "city": "Sydney"}]

for record in records:
    result = collection.insert_one(record)
    print(f"Inserted document with ID: {result.inserted_id}")


print("==============================================================")
print("Total documents in collection:", collection.count_documents({}))

print("==============================================================")

# Fetch all documents
print("Documents in collection:")
for doc in collection.find():
    print(doc)

# Close the connection
client.close()
