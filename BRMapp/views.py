from django.shortcuts import render
from BRMapp import models
from BRMapp.forms import NewBookForm, SearchForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/BRMapp/view-books/')
        else:
            data['error']="Username or Password is incorrect"
            res=render(request,'BRmapp/user-login.html',data)
            return res
    else:
        return render(request,'BRMapp/user-login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMapp/login/')

@login_required(login_url="/BRMapp/login/")
def searchBook(request):
    form=SearchForm()
    username=request.session['username']
    res=render(request,'BRMapp/search-book.html',{'form':form,'username':username})
    return res

@login_required(login_url="/BRMapp/login/")
def search(request):
    form=SearchForm(request.POST)
    username=request.session['username']
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'BRMapp/search-book.html',{'form':form,'books':books,'username':username})
    return res

@login_required(login_url="/BRMapp/login/")
def deleteBook(request):
    bookid=request.GET['bookid']
    #username=request.session['username']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-books')

@login_required(login_url="/BRMapp/login/")
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    username=request.session['username']
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit-book.html',{'form':form,'book':book,'username':username})
    return res

@login_required(login_url="/BRMapp/login/")
def edit(request):
    if request.method=='POST':
        #username=request.session['username']
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMapp/view-books')

@login_required(login_url="/BRMapp/login/")
def viewBooks(request):
    #user = self.request.user
    #books=models.Book.objects.filter(User=request.user)
    #books=models.Book.objects.filter(owner=self.kwargs['pk'])
    username=request.session['username']
    books=models.Book.objects.all()
    res=render(request,'BRMapp/view-books.html',{'books':books,'username':username})
    return res

@login_required(login_url="/BRMapp/login/")
def newBook(request):
    form=NewBookForm()
    username=request.session['username']
    res=render(request,'BRMapp/new-book.html',{'form':form,'username':username})
    return res


@login_required(login_url="/BRMapp/login/")
def add(request):
    if request.method=='POST':
     #username=request.session['username']
     form=NewBookForm(request.POST)
     book=models.Book()
     book.title=form.data['title']
     book.price=form.data['price']
     book.author=form.data['author']
     book.publisher=form.data['publisher']
     book.save()
    s="Record stored<br/><a href='/BRMapp/view-books'>View all books</a>"
    return HttpResponse(s)

# Create your views here.
