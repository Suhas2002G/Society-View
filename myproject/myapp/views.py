from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User        
from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout
# from myapp.models import 
from django.db.models import Q  

def home(request):
    return render(request,'home.html')

