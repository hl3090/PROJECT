from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def login(request):
    return render(request,"myapp/login.html")


def signup(request):
    if request.POST:
        print("Submit button clicked")
        role = request.POST['role']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        print("------------>> role",role)
        print("------------>> usrname",username)
        print("------------>> email",email)
        uid = User.objects.create(email = email,password = password,role=role)
        did = Doctor.objects.create(uid = uid,username = username,contactno = contact)
        if did:
            s_msg = "Successfully Records Added"
            print(s_msg)
        return render(request,"myapp/signup.html")
    else:
        print("SIGNUP page loaded")
        return render(request,"myapp/signup.html")