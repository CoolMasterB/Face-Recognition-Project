import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://face-recog-database-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('students')

data = {
    "202201005":
        {
            "name": "Harsh Belsare",
            "branch": "Computer Engineering",
            "year": 2,
            "roll no": 5
        },
    "202201009":
        {
            "name": "Alvin Devassy",
            "branch": "Computer Engineering",
            "year": 2,
            "roll no": 9
        },
    "202201012":
        {
            "name": "Royston Dsouza",
            "branch": "Computer Engineering",
            "year": 2,
            "roll no": 12
        },
    "202201016":
        {
            "name": "Basil Ferreira",
            "branch": "Computer Engineering",
            "year": 2,
            "roll no": 16
        }
}

for key.value in data.items():
    ref.child(key).set(value)
