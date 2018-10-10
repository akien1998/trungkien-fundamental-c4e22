from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#connect
client =MongoClient(uri)
db = client['c4e']
blog = db['posts']
posts_list = blog.find()
posts ={
    'name':'Vũ Trung Kiên',
    'feelings':'very happy',
    'want to say':"that's great of you",
}
blog.insert_one(posts)
print(posts)

