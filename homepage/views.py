from django.shortcuts import render
from django.http import HttpResponse

boxes = [{'title':'Number 1'}, {'title':'Number 2'}, {'title':'Number 3'}]

for i in range(30):
    boxes.append({'title':f'Number {i+4}'})
# Create your views here.
def mainScreen(request):
    return render(request, "siteRoot/home.html")

def addBook(request):
    return render(request, "siteRoot/addBook.html")

def listBook(request):
    return render(request, "siteRoot/bookList.html", {"boxes":boxes})