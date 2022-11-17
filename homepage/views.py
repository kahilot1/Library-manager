from django.shortcuts import render
from django.http import HttpResponse
from .models import books
from .forms import add_book
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
    #return render(request, "siteRoot/addBook.html")

    if request.method == "POST":
        form = add_book(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            author = form.cleaned_data['author']
            id = form.cleaned_data['id']
            books.objects.create(title=title, summary=summary, author=author, id=id)
            boxes.append({'title':f'{title}', 'id':f'{id}', 'author':f'{author}', 'summary':f'{summary}'})
            print("Book added", title, summary, author, id)
            return render(request, "siteRoot/addBook.html", {'form':add_book(), 'success':True})
        else:
            return render(request, "siteRoot/addBook.html", {'form':form, 'success':False})
    form = add_book()
    return render(request, 'siteRoot/addBook.html', {'form': form})

def listBook(request):
    return render(request, "siteRoot/bookList.html", {"boxes":boxes, 'yes':len(boxes) < 10})

def bookPage(request, book_id):
    return render(request, "siteRoot/bookPage.html", {"book_id":books.objects.get(id=book_id)})