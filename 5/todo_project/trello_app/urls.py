from django.contrib import admin
from django.urls import path , include
from . import views 

urlpatterns = [
    path('index' ,  views.index ,name='index'),
    path('add_list' , views.create_list,name='add_list' ),
    path ('add_task',views.create_task,name='add_task'),
]