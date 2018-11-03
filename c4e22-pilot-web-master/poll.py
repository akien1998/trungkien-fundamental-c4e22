from mongoengine import Document,StringField,ListField

class Poll(Document):
    question1 = StringField()
    question2 = StringField()
    question3 = StringField()
    code = StringField()