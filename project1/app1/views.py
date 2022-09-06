from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def activities(request):
    return render(request,'activities.html')
def blog(request):
    return render(request,'blog.html')
def competition(request):
    return render(request,'competition.html')
def application(request):
    return render(request,'application.html')
def events(request):
    return render(request,'events.html')
def programs(request):
    return render(request,'programs.html')
def register(request):
    return render(request,'register.html')
def staff(request):
    return render(request,'staff.html')















