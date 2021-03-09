from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib.auth import authenticate , login as auth_login ,logout as auth_logout
from django.contrib import messages
from trello_app.models import Test_list,Test
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    user=request.user
   # lists =user.Test_list_set.all()
    lists = Test_list.objects.filter(user = user)
    tasks = Test.objects.filter(list__in = lists)
    return render(request, 'pages/dashboard.html',{'lists':lists , 'tasks':tasks})

def login(request):
    #if request.user.is_authenticated:
    #    return redirect('dashboard')
    if request.method=='POST': 
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        user = authenticate(request,username=Username ,password=Password)
        if user is not None:
            auth_login(request,user)
            #redirect dash board
            return redirect('dashboard')
        else :
           # provide error message
           messages.error(request,'Username or password is incorrect')
           return render(request,'pages/login.html')
    else:
        return render(request,'pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect ('home')
def register(request):
    if request.method == 'POST':
        form=CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            #redirect it to login page
            return redirect('login')
    else :
        form=CreateUserForm()
        return render(request,'pages/register.html',{'form':form})

def home(request):
    return render(request,'pages/home.html')
