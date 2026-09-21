from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def handler(request):
    return HttpResponse(f'Name: {request.GET.get('name')} <br></br> Age: {request.GET.get('age')}')

def handler2(request,val):
    packet = {'booknum':val}
    return render(request,'../templates/bookmodule/index.html',packet)

def getIndex(request,un):
    print(un)
    return render(request,'../templates/bookmodule/index.html',{"name":un})

def handler3(request):
    return HttpResponse('<script> document.querySelector("window").style.backgroundColor = "black" </script>')
