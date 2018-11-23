from mongoengine import Document,StringField
class Poll(Document):
    something = StringField()