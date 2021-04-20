from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    return render(request,'library/login.html')

def signup(request):
    forms=UserCreationForm()
    if request.method=='POST':
        forms=UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            user=forms.cleaned_data.get("username")
            messages.success(request,'account has been created for user '+ user)
            return redirect('login')
    return render(request,'library/signup.html',{'forms':forms,})    

def as_user(request):
    forms=UserCreationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')  

        else:
            messages.info(request,"username or password incorrect")

    return render(request,'library/asuser.html',{'forms':forms,})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):    
    context={

    }
    return render(request,'library/index.html',)

@login_required(login_url='login')
def details(request):
    return HttpResponse("<h1> welcome to details page user</h1>")

