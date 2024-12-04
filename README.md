### How to run
A simple project example that demonstrates how to use MongoDB in a container, with a Python application connecting to it. 
This project sets up a MongoDB container and a Python script to interact with the database.

---

### **Project Structure**
```plaintext
mongodb_project/
│
├── app/
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
└── Dockerfile
```

---

### **Step 1: MongoDB Container Setup**
**`docker-compose.yml`**
```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:6.0
    container_name: mongodb
    ports:
      - "27017:27017"  # Expose MongoDB on localhost
    volumes:
      - mongo_data:/data/db  # Persist data locally

  app:
    build:
      context: .
    depends_on:
      - mongodb
    environment:
      - MONGO_URI=mongodb://mongodb:27017  # Connect to MongoDB service
    volumes:
      - ./app:/usr/src/app
    command: python main.py

volumes:
  mongo_data:
```

---

### **Step 2: Python Application**
**`app/main.py`**
```python
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
```

---

### **Step 3: Python Dependencies**
**`app/requirements.txt`**
```plaintext
pymongo
```

---

### **Step 4: Dockerfile for the Python App**
**`Dockerfile`**
```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /usr/src/app

# Copy and install dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the application
COPY app/ .

# Define the default command
CMD ["python", "main.py"]
```

---

### **Step 5: Run the Project**
1. **Start the containers**:
   ```bash
   docker-compose up --build
   ```
![mongo_db_1.jpg](images%2Fmongo_db_1.jpg)
![mongo_db_2.jpg](images%2Fmongo_db_2.jpg)
![mongo_db_3.jpg](images%2Fmongo_db_3.jpg)

2. **Output**:
   - You’ll see the inserted document's ID and the printed collection content.

3. **Access MongoDB**:
   - You can connect to the MongoDB container using any MongoDB GUI (e.g., Compass) at `localhost:27017`.



### **How It Works**
1. **`docker-compose.yml`**:
   - Defines services for MongoDB and the Python app.
   - Sets up a persistent volume for MongoDB data.

2. **Python Script**:
   - Connects to MongoDB using `pymongo`.
   - Inserts and fetches documents to/from the database.

3. **Environment Variables**:
   - `MONGO_URI` ensures the app dynamically connects to the MongoDB service.

