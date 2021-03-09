from django.shortcuts import render , redirect
from .models import Test_list,Test
from .forms import TestForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    lists= Test_list.objects.all()
    Tests= Test.objects.all()
    return render(request , 'trello_app/index.html',{'lists':lists , 'Tests':Tests})

@login_required(login_url='login')
def create_list(request):
    if request.method == 'POST':
        list_name=request.POST['list_name']
        list=Test_list(name=list_name , user=request.user)
        list.save()
        return redirect('dashboard')
    else:
      return render(request , 'trello_app/new_list.html')


@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
      form=TestForm(data=request.POST)
      form.save()
      return redirect('dashboard')
    else:
        form=TestForm()
        return render(request , 'trello_app/new_task.html',{'forms':form})

    
