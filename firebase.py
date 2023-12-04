import firebase_admin
from firebase_admin import db, credentials


cred = credentials.Certificate("./firebase_auth.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://passkeeper-9e444-default-rtdb.firebaseio.com/"})



def add_to_database(arr,service,username):
  ref = db.reference("/"+service+"/"+username)
  ref.set(arr)


def delete_database():
  ref = db.reference("/")
  ref.delete()

def delete_selected_pass(service,username):
  ref=db.reference("/"+service+"/"+username)
  ref.delete()

def get_database(service,username):
  ref=db.reference("/"+service+"/"+username)
  return ref.get()

def update_selected_pass(service,username,password):
  ref=db.reference("/"+service+"/"+username)
  ref.update(dict({'password':password}))


#Test Command
# add_to_database(dict({'password': 'wqfCisOJwrs='}),"ef","pjk")
# ref = db.reference("/")
# print(ref.get())
#update_selected_pass("ef","pjk","new")
# print(ref.get())