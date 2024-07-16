from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'AMTSapp/index.html')

def login(request):
    return render(request,"AMTSapp/login.html")


def signup(request):
    return render(request,"AMTSapp/signup.html")


def user_dashboard(request):
    pass



def administrator_dashboard(request):
    pass

