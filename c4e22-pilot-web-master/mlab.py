import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds013966.mlab.com:13966/c4e22-poll

host = "ds013966.mlab.com"
port = 13966
db_name = "c4e22-poll"
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