from django.shortcuts import render
from django.http import HttpResponse
from .models import books
boxes = []
ls = books.objects.all()
for i in ls:
    boxes.append({'title':f'{i.title}', 'id':f'{i.id}', 'author':f'{i.author}', 'summary':f'{i.summary}'})

# {'title':'Number 1'}
#for i in range(30):
#    boxes.append({'title':f'Number {i+4}'})
# Create your views here.
def mainScreen(request):
    return render(request, "siteRoot/home.html")

def addBook(request):
    return render(request, "siteRoot/addBook.html")

def listBook(request):
    return render(request, "siteRoot/bookList.html", {"boxes":boxes, 'yes':len(boxes) < 10})

def bookPage(request, book_id):
    return render(request, "siteRoot/bookPage.html", {"book_id":books.objects.get(id=book_id)})