import firebase_admin #pip install firebase_admin
from firebase_admin import firestore, credentials
import pyrebase #pip install pyrebase


firebaseconfig = {
    "apiKey": "AIzaSyCjLiNVCxHNggIaqVaHFSFKn2Uf_UiOH2k",
    "authDomain": "flaskapi-bcd20.firebaseapp.com",
    "projectId": "flaskapi-bcd20",
    "storageBucket": "flaskapi-bcd20.appspot.com",
    "messagingSenderId": "1037291710285",
    "databaseURL": "https://flaskApi.firebaseio.com",
    "appId": "1:1037291710285:web:70ee99159c2fd23c9a7904",
    "measurementId": "G-QXM50GE189"
}
firebase = pyrebase.initialize_app(firebaseconfig)
firebase_db = firebase.database()

auth = firebase.auth()

cred = credentials.Certificate("/Users/mountainlabs/apiWithFlask/src/config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
