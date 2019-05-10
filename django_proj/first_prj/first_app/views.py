from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    # return HttpResponse("<h1>Hello</h1>")
    my_dictionaty = {"my_insert": "myRender new response"}
    return render(req, 'first_app/index.html',context=my_dictionaty)

def help(req):
    my_dict = {"help":"help page"}
    return render(req, 'help/index.html',context=my_dict)
