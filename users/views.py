from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'users/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username , password = password)
        if user is not None :
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'users/login.html',{
                "message":"Invalid User Please Register"
            })
    return render(request,'users/login.html')
        
def register_view(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request,username = username , password = raw_password)
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{
        'form' : form,
    })




def logout_view(request):
    logout(request)
    return render(request,'users/login.html',{
        "message":"Loged Out"
    })
