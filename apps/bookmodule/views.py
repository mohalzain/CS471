from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
path = os.getcwd()
links = {"l1":"index.html","l2":'list_books.html',"l3":'aboutus.html'}
def indexHandler(request):
    print(path)
    return render(request, f'index.html')

def list_booksHandlers(request):
    return render(request, f'list_books.html')


def oneBookHandler(request):
    return render(request, f'one_book.html')

def aboutUsHandler(request):
    return render(request, f'aboutus.html')