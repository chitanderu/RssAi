from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request,"../templates/login.html")