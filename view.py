# import pyrebase
import firebase
# from collections.abc import Mapping
from flet import *
from main import _moduleList
from datetime import datetime


CONFIG = {
  "apiKey": "AIzaSyBfH4d5A6rc8lcM6AMmSmf4lRQQfbAzenQ",
  "authDomain": "flet-cb-mobileapp.firebaseapp.com",
  "projectId": "flet-cb-mobileapp",
  "storageBucket": "flet-cb-mobileapp.appspot.com",
  "messagingSenderId": "896214009084",
  "appId": "1:896214009084:web:4e765eab897d12146dc379",
  "databaseURL": "https://flet-cb-mobileapp-default-rtdb.asia-southeast1.firebasedatabase.app/",
}

global SESSION
SESSION = {}

firebase = firebase.initialize_app(CONFIG)
auth = firebase.auth()
db = firebase.database()



def ChangeRoute(e, page_route):
    global _moduleList
    e.page.views.clear()

    if page_route == "/register":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_()
        )
        e.page.go("/register")

    if page_route == "/login":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_()
        )
        e.page.go("/login")
        e.page.go("/register")
    else:
        pass
    
    e.page.update()

# Create a User using Registration form
def RegisterUser(e):
    for page in e.page.views[:]:
        if page.route == "/register":
            res = page.controls[0].controls[0].content.controls[4]
            try:
                print(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )
                # use firebase auth API to signUp a new User with email and Pass
                auth.create_user_with_email_and_password(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )

                data = {
                    "firstName" : res.controls[0].content.value,
                    "lastName" : res.controls[1].content.value,
                    "email" : res.controls[2].content.value,
                    # "password" : res.controls[3].content.value,
                }

                db.child("users").push(data)

                e.page.views.clear()
                e.page.views.append(
                _moduleList['/login'].loader.load_module()._view_())
                e.page.update()

            except Exception as ex:
                print(ex)
            finally:
                for item in res.controls[:]:
                    item.content.value = None
                    item.content.update()


def ShowMenu(e):
    for page in e.page.views[:]:
        if page.route == '/home' :
            if e.data == 'true':
                page.controls[0].controls[0].controls[0].controls[0].width = 185
                page.update()
            else:
                page.controls[0].controls[0].controls[0].controls[0].width = 60
                page.update()

def logInUser(e):
    print("Inside LoginUser")
    first_name, last_name = GetUserDetail(e)
    print(first_name, last_name)

    if first_name != None and last_name != None:
        e.page.views.clear()
        e.page.views.append( _moduleList['/home'].loader.load_module()._view_(first_name, last_name) )
        e.page.go('/home')
        e.page.update()
    else:
        print("EmailID and Password is Wrong..!!")
        


def GetUserDetail(e):
    print("Inside GetUserDetails")
    global _moduleList
    for page in e.page.views[:]:
        if page.route == '/login':
            # text fireld of parent control
            res = page.controls[0].controls[0].content.controls[4]
            try:
                # here we autheticate the user using email & pass
                user = auth.sign_in_with_email_and_password(
                    res.controls[0].content.value,
                    res.controls[1].content.value,
                )

                SESSION["users"] = user

                val = db.child("users").get()
                print(val)

                for i in val:
                    if i.val()["email"] == user["email"]:
                        first_name = i.val()["firstName"]
                        last_name = i.val()["lastName"]
                        SESSION["path"] = i.key()
                        SESSION["firstName"] = first_name
                        SESSION["lastName"] = last_name   
                        
                        return [first_name, last_name]

            except Exception as ex:
                print(ex)
    print("No matching Email...")
    return None
    
