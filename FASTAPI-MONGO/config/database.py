from motor.motor_asyncio import AsyncIOMotorClient

client=AsyncIOMotorClient("mongodb://localhost:27017/")

db= client['db_todo']
collection_name = db['dummy_collection']
  





'''from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client['todo_db']

collection_name = db['todo_collections']'''








# def connect_to_mongodb():
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['mydatabase']
#     return db

# def create_collection(db):
#     collection = db['mycollection']
#     return collection

# def insert_document(collection):
#     document = {
#         'name': 'John Doe',
#         'age': 30,
#         'city': 'New York'
#     }
#     collection.insert_one(document)
#     print('Document inserted successfully.')

# def find_documents(collection):
#     documents = collection.find()
#     for document in documents:
#         print(document)

# def update_document(collection):
#     filter = {'name': 'John Doe'}
#     update = {'$set': {'age': 31}}
#     collection.update_one(filter, update)
#     print('Document updated successfully.')
    
# def delete_document(collection):
#     filter = {'name': 'John Doe'}
#     collection.delete_one(filter)
#     print('Document deleted successfully.')

# if __name__ == '__main__':
#     db = connect_to_mongodb()
#     collection = create_collection(db)
    
#     insert_document(collection)
#     find_documents(collection)
    
#     update_document(collection)
#     find_documents(collection)
    
#     delete_document(collection)
#     find_documents(collection)
    
#     db.drop_collection('mycollection')
#     print('Collection dropped successfully.')
#     client.close()

