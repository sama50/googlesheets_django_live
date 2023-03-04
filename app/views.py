from django.shortcuts import render
import uuid
# Create your views here.

def index(request):

    return render(request,'index.html',{'uuid':uuid})

def home(request,id):

    return render(request,'home.html',{'idurl':id})