import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate("scrum-project/firebase_config/firebase_admin_sdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://campuslink-56ae6-default-rtdb.firebaseio.com'
    
})


# Function to set data in Firebase
def set_data(ref_path, data):
    ref = db.reference(ref_path)
    ref.set(data)

# Function to update data in Firebase
def update_data(ref_path, data):
    ref = db.reference(ref_path)
    ref.update(data)

# Function to get data from Firebase
def get_data(ref_path):
    ref = db.reference(ref_path)
    return ref.get()

# Function to delete data from Firebase
def delete_data(ref_path):
    ref = db.reference(ref_path)
    ref.delete()

def push_data(ref_path, data):
    ref = db.reference(ref_path)
    return ref.push(data)
