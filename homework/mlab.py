import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds137370.mlab.com:37370/data3

host = "ds137370.mlab.com"
port = 37370
db_name = "data3"
user_name = "admin"
password = "vutrungkien1998"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())