from mongoengine import Document, IntField,StringField, ReferenceField
class Vote(Document):
    choice = IntField()
    voter  = StringField()
    poll = ReferenceField("Poll")
    # tro thang den thang Poll