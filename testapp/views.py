from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import employee
# Create your views here.
def greeting(request):
    s="<h1>Hello there ! this is my first app</h1><p>Hi there! this is a paragraph"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Tushar Mittal</h1>"
    s+="<h2>Mobile:7830599885</h2>"
    return HttpResponse(s)
def about(request):
    s="<h1>I am keen to learn new things so that one day i can create new things<h1> "
    res1=render(request,'testapp/about.html')
    return res1
def employee_info_view(request):
    employees=employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
