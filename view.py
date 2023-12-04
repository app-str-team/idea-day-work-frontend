# import pyrebase
import firebase
# from collections.abc import Mapping
from flet import *
from main import _moduleList
from datetime import datetime
import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
config_file = os.path.join(__location__, 'connectionstring.json')

CONFIG = {}

with open(config_file, 'r') as f:
    CONFIG = json.load(f)
    
print(CONFIG)

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
        # e.page.go("/register")
    else:
        pass

    if page_route == "/postComments":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_()
        )
        e.page.go("/postComments")

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
                    "password" : res.controls[3].content.value,
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

# logIn in App
def logInUser(e):
    print("Inside LoginUser")
    first_name, last_name = GetUserDetail(e)
    print(first_name, last_name)

    if first_name != None and last_name != None:
        e.page.views.clear()
        e.page.views.append( _moduleList['/home'].loader.load_module()._view_(e.page) )
        e.page.go('/home')
        e.page.update()
    else:
        print("EmailID and Password is Wrong..!!")


# def LogOutUser(e):
#     e.page.SESSION.clear()
#     e.page.go('/login') 
#     e.page.update()

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
    return [None, None]

# This function is for to post the judges comments on firebase.
def PostJudgeScore(e):
    for page in e.page.views[:]:
        if page.route == '/postComments':
            res = page.controls[0].controls[0].content.controls[4]
            print(type(res))
            try:
                # print(
                #     res.controls[0].content.value,
                #     res.controls[1].content.value,
                #     res.controls[2].content.value,
                #     res.controls[3].content.value,
                #     res.controls[4].content.value,
                #     res.controls[5].content.value,
                # )

                judgeData = {
                    "ideaPitch":res.controls[0].content.value,
                    "efficiencyValue":res.controls[1].content.value,
                    "featureScope":res.controls[2].content.value,
                    "presentation":res.controls[3].content.value,
                    "workingModel":res.controls[4].content.value,
                    "judgeComment":res.controls[5].content.value,
                }

                db.child('judgesComments').push(judgeData)
                e.page.views.clear()
                e.page.views.append(
                _moduleList['/postComments'].loader.load_module()._view_())
                e.page.update()
            
            except Exception as ex:
                print(ex)

def homePage(e):
        e.page.views.clear()
        e.page.views.append( _moduleList['/home'].loader.load_module()._view_() )
        e.page.go('/home')
        e.page.update()
  
# User ability to post comment
# def PostText(e, first_name:str, last_name:str):
#     post_date = datetime.now().strftime("%b %d, %y %I:%M")

#     for page in e.page.views[:]:
#         if page.route =='/home':
#             res = page.controls[0].controls[0].controls[2].controls[3].controls[0]

#             # here we set the data in dict
#             data = {
#                 "firstName" : first_name,
#                 "lastName" : last_name,
#                 "postDate" : post_date,
#                 "comment" : res.content.controls[0].content.value,
#             }

#             ref_data = (
#                 db.child("users"+"/"+SESSION["path"]).child("comments").push(data)
#             )
#             # .child("comments") will create a new table

#             page.controls[0].controls[0].controls[2].controls[3].controls.append(
#                 postComment.DisplayPost(
#                     first_name,
#                     last_name,
#                     post_date,
#                     res.content.controls[0].content.value,
#                     ref_data['name'],
#                 )
#             )

#             res.content.controls[0].content.value = None
#             res.content.controls[0].content.update()
#             e.page.update()