from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import empuser
from .models import empdata
from django.contrib.auth.hashers import make_password,check_password
import re


def pwd(password):
    if (len(password)<=8):
        return False
    elif not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password) or not re.search(r"\d",password):
        return False
    elif not re.search(r"[@#_$%^&*<>]",password):
        return False
    else:
        return True


def signup(request):
    if request.method=="POST":
        name=request.POST["username"]
        password=request.POST["password"]
        verifyuser=empuser.objects.filter(username=name).exists()
        if verifyuser:
            return HttpResponse ("username alread exist")                  
        else:          
            if not pwd(password):
                return HttpResponse("Password should be at least 8 characters long and contain uppercase, lowercase, digit, and special characters.")
            else:
                has_pwd=make_password(password)  
                user=empuser()
                user.username=name
                user.password=has_pwd
                user.save()
                return redirect("login")
    return render(request, "signup.html")


def login(request):
    if request.method=="POST":
        name=request.POST["username"]
        pwd=request.POST["password"]
        verifyuser2=empuser.objects.get(username=name)
        ch_pwd=check_password(pwd,verifyuser2.password)        
        if verifyuser2.username and ch_pwd:
            request.session['user']=name
            return redirect("tables")
        else:
            return HttpResponse('please enter valid username or password.')
    return render(request,"login.html")

def insert(request):
    if request.method=="POST":
        name=request.POST["name"]
        regno=request.POST["regno"]
        age=request.POST["age"]
        yearofjoin=request.POST["yearofjoin"]
        mobile=request.POST["mobileno"]
        place=request.POST["place"]
        emp=empdata()
        emp.name=name
        emp.regno=regno
        emp.age=age
        emp.yearofjoin=yearofjoin
        emp.mobile=mobile
        emp.address=place
        emp.save()
        return redirect("tables")
    return render(request,"insert.html")

def tables(request):
    if 'user' in request.session:
        crt_user=request.session['user']
        verifyuser=empdata.objects.filter(name=crt_user).values()
    return render(request,"index.html",{"emp":verifyuser})

def edit(request,id):
    singleemp=empdata.objects.get(id=id)
    if request.method=="POST":
        name=request.POST["name"]
        regno=request.POST["regno"]
        age=request.POST["age"]
        yearofjoin=request.POST["yearofjoin"]
        mobile=request.POST["mobileno"]
        place=request.POST["place"]

        singleemp.name=name
        singleemp.regno=regno
        singleemp.age=age
        singleemp.yearofjoin=yearofjoin
        singleemp.mobile=mobile
        singleemp.address=place
        singleemp.save()
        return redirect("tables")
    return render(request,"edit.html",{"singleemp":singleemp})

def delete(request,id):
    singleemp=empdata.objects.get(id=id)
    singleemp.delete()
    return redirect("tables")

def logout(request):
    del request.session['user']
    return redirect("login")


