from django.shortcuts import render
from django.http import HttpResponse
from .models import books
from .forms import add_book, checkinoutBook
from django.db.models import Q

boxes = []
# {'title':'Number 1'}
#for i in range(30):
#    boxes.append({'title':f'Number {i+4}'})
# Create your views here.
def isPartOfGroup(user, group_name):
    return user.groups.filter(name=group_name).exists()
def mainScreen(request):
    return render(request, "siteRoot/home.html", {'isPartOf':isPartOfGroup(request.user, 'librarian')})

def addBook(request):
    #return render(request, "siteRoot/addBook.html")
    if isPartOfGroup(request.user, 'librarian'):

        if request.method == "POST":
            form = add_book(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                summary = form.cleaned_data['summary']
                author = form.cleaned_data['author']
                id = form.cleaned_data['id']
                if ' ' in id:
                    xyz = list(id)
                    for y, i in enumerate(xyz):
                        if i == ' ':
                            xyz[y] = '_'
                    id = ''.join(xyz)
                books.objects.create(title=title, summary=summary, author=author, id=id)
                print("Book added", title, summary, author, id)
                return render(request, "siteRoot/addBook.html", {'form':add_book(), 'success':True, 'isPartOf':isPartOfGroup(request.user, 'librarian')})
            else:
                return render(request, "siteRoot/addBook.html", {'form':form, 'success':False, 'isPartOf':isPartOfGroup(request.user, 'librarian')})
        form = add_book()
        return render(request, 'siteRoot/addBook.html', {'form': form, 'isPartOf':isPartOfGroup(request.user, 'librarian')})
    return render(request, 'siteRoot/home.html' , {'isPartOf':isPartOfGroup(request.user, 'librarian')})

def listBook(request):
    boxes = []
    box= []
    from .models import books
    ls = books.objects.all()
    for i in ls:
        boxes.append({'title':f'{i.title}', 'id':f'{i.id}', 'author':f'{i.author}', 'summary':f'{i.summary}'})
        box.append(i)
    return render(request, "siteRoot/bookList.html", {"boxes":boxes, 'yes':len(boxes) < 10, 'box':box, 'isPartOf':isPartOfGroup(request.user, 'librarian')})

def bookPage(request, book_id):
    booky = books.objects.get(id=book_id)
    if request.method == "GET":
        print('Getting data and proccessing', request.GET)
        if booky.checked_out:
            text = 'Check In'
        else:
            text='Check Out'
        form = checkinoutBook(text, request.GET)
        print('Data is Valid')
        if form.is_valid():
            if text == 'Check Out':
                text = 'Check In'
                booky.checked_out = True
                booky.book_owner = form['User'].value().strip()
                booky.save()
                form = checkinoutBook(text)
        else:
            text = 'Check Out'
            booky.checked_out = False
            booky.book_owner = "Librarian"
            booky.save()
            form = checkinoutBook(text)

        
        return render(request, 'siteRoot/bookPage.html', {'book_id':booky, 'form':form, 'isPartOf':isPartOfGroup(request.user, 'librarian')})
    if booky.checked_out:
        form = checkinoutBook()
    else:
        form = checkinoutBook('Check Out')
    return render(request, "siteRoot/bookPage.html", {"book_id":booky, 'isPartOf':isPartOfGroup(request.user, 'librarian'), 'form':form})

def search(request):
    query = None
    result = []
    result1 = []
    if request.method == "GET":
        query = request.GET.get("search")
        result = books.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        result1 = (books.objects.filter(id__icontains=query))
        result2 = []
        for xy, i in enumerate(result1):
            if i.id == query:
                result2.append(result1[xy])
    return render(request, 'siteRoot/search.html', {'query':query, 'result':result, 'yes':len(result) < 10, 'result1':result2,  'isPartOf':isPartOfGroup(request.user, 'librarian')})