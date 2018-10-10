from pymongo import MongoClient
uri ="mongodb://admin:vutrungkien1998@ds125293.mlab.com:25293/sesson5"
#conection 
client =MongoClient(uri)
db = client.get_default_database()
posts = db['post'] # teen ngan tu 
post_list = posts.find()
#p = post_list[0]
for p in post_list:
    print(p['author'])
    print(p['type'])
    print(p['content'])

# creat a document
# post={
#     'type':'hôm nay trời mua',
#     'content':'nha làm bài tập',
#     'author':'me',
# }
# # insert creat document
# posts.insert_one(post)




