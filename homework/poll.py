from mongoengine import Document,StringField,ListField

class Poll (Document):
    first = StringField()
    last = StringField()
    coure = StringField()
    code = StringField()