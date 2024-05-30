from pymongo import MongoClient

conn = MongoClient()  #"mongodb://localhost:27017/test" #this is the path inside that MongoClient() we dont need to write in that as it is their by default so if we dont write this its okay  #if online cluster you are using then provide that path here

db = conn.local