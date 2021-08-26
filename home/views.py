from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'index1.html')

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        print(a)
        return render(request,"buynow.html")

    return render(request,"buynow.html")

def login(request):
    if request.method =='POST':
        email =request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        if user is not None:
            return render(request,'buynow.html')
        else:
            context={'message':'Email or Password dose not match','class':'danger'}
            return render(request,'login.html',context)
    return render(request,'login.html')
            
def register(request):
    context1 = {'message1':'Login has been created','class':'success'}
    if request.method=="POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        password =request.POST.get("password")
        print(email,name,mobile)

        check_user=User.objects.filter(email=email).first()
        check_profile=Profile.objects.filter(mobile=mobile).first()
    
        if check_user or check_profile:
            context={'message':'User already exists','class':'danger'}
            return render(request,'register.html',context)
        else:
            user =User.objects.create_user(username=email,email=email,password=password)
            user.save()
            print("user_created")
            profile = Profile(user=user ,mobile=mobile)
            profile.save()
            print("profile created")
            return render(request,'register.html',context1)
       
        # user=User(email=email ,first_name=name)
        # user.save()
    return render(request,'register.html')
