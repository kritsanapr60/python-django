from django.http import HttpResponse
#from .models import Entry
from pyrebase import pyrebase 
import pyrebase 
from django.shortcuts import render
from django.contrib import auth

config = {
    'apiKey': "AIzaSyDZJU3DVrCR9Ra3KJpv-_JxyFQZojDdxsQ",
    'authDomain': "kritsana-fed6b.firebaseapp.com",
    'databaseURL': "https://kritsana-fed6b.firebaseio.com",
    'projectId': "kritsana-fed6b",
    'storageBucket': "kritsana-fed6b.appspot.com",
    'messagingSenderId': "303968917811"
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

def signIn(req):

    return render(req, 'myapp/signIn.html')

def postsign(req):
    email=req.POST.get('email')
    passw = req.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(req,'myapp/signIn.html',{"messg":message})
    print(user['idToken'])
    session_id=user['idToken']
    req.session['uid']=str(session_id)
    return render(req, 'myapp/welcom.html',{"e":email})

def logout(req):
    auth.logout(req) 
    return render(req, 'myapp/index.html')

def signUp(req):
    return render(req,"myapp/signup.html")

def postsignup(req):
    name=req.POST.get('name')
    email=req.POST.get('email')
    passw=req.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"name":name,"status":"0"}
        database.child("users").child(uid).child("details").set(data) #ยังไม่ได้ create data base
    except:
        message="Unable to create account try again"
        return render(req,"myapp/signup.html",{"messg":message})
    
    return render(req,"myapp/signIn.html")

#def Clams(request):
  #return render(request, 'myapp/Clams.html')
#def index(req):
    #entries = Entry.objects.all()
    #return render(req, 'myapp/index.html', { 'entries': entries })
def index(req):
    return render(req, 'myapp/index.html')

def chap1(req):
    return render(req, 'myapp/chap1.html')

def chap2(req):
    return render(req, 'myapp/chap2.html')

def chap3(req):
    return render(req, 'myapp/chap3.html')

def chap4(req):
    return render(req, 'myapp/chap4.html')

def chap5(req):
    return render(req, 'myapp/chap5.html')

def chap6(req):
    return render(req, 'myapp/chap6.html')

def chap7(req):
    return render(req, 'myapp/chap7.html')

def chap8(req):
    return render(req, 'myapp/chap8.html')

def chap9(req):
    return render(req, 'myapp/chap9.html')

def chap10(req):
    return render(req, 'myapp/chap10.html')

def chap11(req):
    return render(req, 'myapp/chap11.html')

def chap12(req):
    return render(req, 'myapp/chap12.html')

def chap13(req):
    return render(req, 'myapp/chap13.html')

def chap14(req):
    return render(req, 'myapp/chap14.html')

def chap15(req):
    return render(req, 'myapp/chap15.html')

def chap16(req):
    return render(req, 'myapp/chap16.html')