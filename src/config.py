import firebase_admin #pip install firebase_admin
from firebase_admin import firestore, credentials
import pyrebase #pip install pyrebase


firebaseconfig = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "databaseURL": "",
    "appId": "",
    "measurementId": ""
}
firebase = pyrebase.initialize_app(firebaseconfig)
firebase_db = firebase.database()

auth = firebase.auth()

cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
