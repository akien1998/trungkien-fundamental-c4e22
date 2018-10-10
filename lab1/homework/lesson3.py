from pymongo import MongoClient
from matplotlib import pyplot
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client =MongoClient(uri)
db = client['c4e']
blog = db['customers']
customers_list = blog.find()
sum={
    "events":0,
    "wom":0,
    "ads":0,
}
for i in customers_list:
    if i["ref"]=="events":
        sum["events"] =sum["events"]+1
    elif i["ref"]=="wom":
        sum["wom"]= sum["wom"] +1
    elif i["ref"]=="ads":
        sum["ads"]= sum["ads"]+1
print("sum events = ",sum["events"])
print("sum wom = ",sum["wom"])
print("sum ads = ",sum["ads"])

# part 2
machine_count =[3902,1132,1938]
machine_name =["Events","Wom","ADS"]
pyplot.pie(machine_count, labels=machine_name, autopct="%.1f%%",shadow=True)
pyplot.title("Events vs Wom vs ADS")
pyplot.axis("equal")
pyplot.show()
