
from flet import *
from main import _moduleList
from datetime import datetime
import json
import requests
from common import usersession

'''
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
'''


def ChangeRoute(e, page_route):
    global _moduleList
    e.page.views.clear()

    if page_route == "/register":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_(e.page)
        )
        e.page.go("/register")

    if page_route == "/login":
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_(e.page)
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
                '''
                # use firebase auth API to signUp a new User with email and Pass
                auth.create_user_with_email_and_password(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )
                '''
                resp = requests.post(url="http://127.0.0.1:5000/createuser",
                         json={
                               "display_name":res.controls[0].content.value,
                               "email":res.controls[1].content.value, 
                               "password":res.controls[2].content.value
,
                              },
                         headers={"Content-Type":"application/json"})
                
                print("resp =", resp.json() )
                
                '''
                data = {
                    "firstName" : res.controls[0].content.value,
                    "lastName" : res.controls[1].content.value,
                    "email" : res.controls[2].content.value,
                    "password" : res.controls[3].content.value,
                }
                db.child("users").push(data)
                '''
                e.page.views.clear()
                e.page.views.append(
                _moduleList['/login'].loader.load_module()._view_(e.page))
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
    display_name, uid = GetUserDetail(e)
    print(display_name, display_name)

    if display_name != None and uid != None:
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
                '''
                user = auth.sign_in_with_email_and_password(
                    res.controls[0].content.value,
                    res.controls[1].content.value,
                )
                '''
                resp = requests.post(url="http://127.0.0.1:5000/signin",
                         json={
                               "email":res.controls[0].content.value, 
                               "password":res.controls[1].content.value
                              },
                         headers={"Content-Type":"application/json"})
                
                user = {'displayName': resp.json()['displayName'], 
                        'uid': resp.json()['localId'] ,
                        'idToken': resp.json()['idToken'],
                        'userRole':resp.json()['userRole'] }
                        
                usersession.SESSION['active_session'] = user
                
                print("userRole =", resp.json()['userRole'])
                

                return user['displayName'], user['uid']
                '''
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
                '''
            except Exception as ex:
                print(ex)
    #print("No matching Email...")
    return [None, None]
      

# This function is for to post the judges comments on firebase.
def PostJudgeScore(e):
    for page in e.page.views[:]:
        if page.route == '/postComments':
            res = page.controls[0].controls[0].content.controls[4]
            print(type(res))
            try:
                judgeData = {
                    res.controls[0].content.label:res.controls[0].content.value,
                    res.controls[1].content.label:res.controls[1].content.value,
                    res.controls[2].content.label:res.controls[2].content.value,
                    res.controls[3].content.label:res.controls[3].content.value,
                    res.controls[4].content.label:res.controls[4].content.value,
                    res.controls[5].content.label:res.controls[5].content.value,
                    'id':usersession.SESSION['active_session']['selectedIdeaID'],
                    'judge_uid':usersession.SESSION['active_session']['uid']
                }
                response = requests.post(url="http://127.0.0.1:5000/postscore",
                            json = judgeData,
                         headers={"Content-Type":"application/json"})
                '''
                e.page.views.clear()
                e.page.views.append(
                _moduleList['/postComments'].loader.load_module()._view_(e.page))
                e.page.update()
                '''
                if (response.json()['status'] == 'OK'):
                    e.page.snack_bar = SnackBar(Text(f"Successfully posted the judgement. Taking back to ideas" ))
                else:
                    e.page.snack_bar = SnackBar(Text(f"Some error occured while submitting the judgement" ))
                e.page.snack_bar.open = True  
                
                e.page.update()    
    
                goToPreviousPage(e)    
                
            except Exception as ex:
                print(ex)

def goToPreviousPage(e):
    e.page.views.pop()
    top_view = e.page.views[-1]
    e.page.go(top_view.route)
    
def homePage(e):
        e.page.views.clear()
        e.page.views.append( _moduleList['/home'].loader.load_module()._view_(e.page) )
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