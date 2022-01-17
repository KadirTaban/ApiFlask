from src.config import db
class Users():
    key = None
    uuid = None
    name = None
    surname = None
    bio = None
    def __init__(self,key=None,uuid=None,name = None,surname=None, bio = None):
        self.uuid = uuid
        self.name = name
        self.surname = surname
        self.bio = bio

    def add_user(self):
        data = {'uuid': self.uuid,'name': self.name,'surname':self.surname,'bio':self.bio}
        db.collection('users').add(data)

    def get_user(self,uuid):
        users = db.collection('users').where('uuid','==',uuid ).get()

        key = users[0].id

        userDict = users[0].to_dict()
        self.key = key
        self.uuid = userDict['uuid']
        self.name = userDict['name']
        self.surname = userDict['surname']
        self.bio = userDict['bio']

        return self

    def update_user(self,key):
        db.collection('users').document(self.key).update({'uuid': self.uuid, 'name': self.name, 'surname': self.surname, 'bio': self.bio})



