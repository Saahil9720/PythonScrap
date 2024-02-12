from pymongo import MongoClient

# Replace the following variables with your own values
your_connection_string = "mongodb+srv://saahilvekariya20:LpXBKo9Ot9wXoxo1@cluster0.jexg3i0.mongodb.net/?retryWrites=true&w=majority"
db_name = "PythonScrap"
collection_name = "Test"

# Connect to MongoDB Atlas
client = MongoClient(your_connection_string)

# Select the database
db = client[db_name]

# Select the collection
collection = db[collection_name]

# Data to insert
data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

# Inserting data into the collection
insert_result = collection.insert_one(data)
print(f"Data inserted with id {insert_result.inserted_id}")

# Retrieve and print all documents from the collection
for document in collection.find():
    print(document)
