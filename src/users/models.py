from src.config import db
class Users():
    key = None
    uuid = None
    name = None
    surname = None
    skill = None
    def __init__(self,key=None,uuid=None,name = None,surname=None, skill = None):
        self.key = key
        self.uuid = uuid
        self.name = name
        self.surname = surname
        self.skill = skill

    def add_user(self):
        data = {'uuid': self.uuid,'name': self.name,'surname':self.surname,'skill':self.skill}
        db.collection('users').add(data)

    def get_user(self,uuid):
        users = db.collection('users').where('uuid','==',uuid).get()

        key = users[0].id

        userDict = users[0].to_dict()
        self.key = key
        self.uuid = userDict['uuid']
        self.name = userDict['name']
        self.surname = userDict['surname']
        self.skill = userDict['skill']

        return self

    def update_user(self,key):
        db.collection('users').document(key).update({'uuid': self.uuid, 'name': self.name, 'surname': self.surname, 'skill': self.skill})

    def delete_user(self):
        db.collection('users').document(self.key).delete()

