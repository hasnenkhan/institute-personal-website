from pymongo import MongoClient

cluster = MongoClient(
"mongodb+srv://kashif:L6r4999-7GKBRWu@cluster0.y5vjc.mongodb.net/certificate_verification?retryWrites=true&w=majority")
db = cluster["certificate_verification"]
collections = db["certificate_verification"]
collections2 = db["users"]