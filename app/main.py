import os
from pymongo import MongoClient

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# Connect to the database and collection
db = client.my_database
collection = db.my_collection

# Insert a document
sample_data = {"name": "Alice", "age": 25, "city": "New York"}
result = collection.insert_one(sample_data)
print(f"Inserted document with ID: {result.inserted_id}")

# Fetch all documents
print("Documents in collection:")
for doc in collection.find():
    print(doc)

# Close the connection
client.close()
