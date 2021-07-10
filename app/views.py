from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    books = Book.objects.filter(status='a')
    ctx= {
        'books': books,
        'title':'dashboard'
    }
    return render(request, 'users/dashboard.html', ctx)     

@login_required
def contact(request):
    form = ContactForm()
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'contact information saved successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'error saving contact information')
    ctx = {'form': form,'title': 'Contact Us'}
    return render(request, 'users/contact.html', ctx)     

@login_required
def report(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'report saved successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'error saving report')
    ctx = {'form': form,'title': 'Report a Problem'}
    return render(request, 'users/report.html', ctx)

@login_required
def profileview(request):
    try:
        profile = Profile.objects.get(user=request.user)
        ctx ={
            'title':'profile',
            'profile':profile,
        }
        return render(request,'users/view_profile.html',context= ctx)
    except Exception as e:
        print(e)
        ctx ={'title':'profile'}
        messages.success(request,'You have not created a profile yet')
        return redirect('profile_edit')

@login_required
def profile_edit(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
    except:
        profile = None
        form = ProfileForm()

    if request.method == 'POST':
        if profile:
            form = ProfileForm(request.POST,request.FILES,instance=profile)
        else:
            form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            
            messages.success(request,'Profile updated successfully')
            return redirect('profile_view')
        else:
            print(form.errors)
            messages.error(request,'Error updating your profile')
    ctx ={
        'title':'profile edit',
        'form':form,
    }
    return render(request,'users/edit_profile.html',context= ctx)

@login_required
def book_add(request):        
    form = BookForm()
    if request.method == 'POST':     
        form = BookForm(request.POST,request.FILES)     
        if form.is_valid():     
            book = form.save(commit=False)     
            book.user = request.user     
            book.save()     
            messages.success(request,'Book added successfully')     
            return redirect('book_list')     
        else:     
            messages.error(request,'Error adding book')     
    ctx = {'form':form,'title':'Add Book'}     
    return render(request,'books/add_book.html',context=ctx)     

@login_required
def book_list(request):
    books = Book.objects.all()
    ctx = {'books':books,'title':'Book List'}
    return render(request,'books/book_list.html',context=ctx)

@login_required
def book_edit(request,pk):
    book = get_object_or_404(Book,pk=pk)     
    form = BookForm(instance=book)     
    if request.method == 'POST':     
        form = BookForm(request.POST,request.FILES,instance=book)     
        if form.is_valid():     
            book = form.save(commit=False)     
            book.user = request.user     
            book.save()     
            messages.success(request,'Book updated successfully')     
            return redirect('book_list')     
        else:     
            messages.error(request,'Error updating book')     
    ctx = {'form':form,'title':'Edit Book'}     
    return render(request,'books/edit_book.html',context=ctx)

@login_required
def book_delete(request,pk):     
    book = get_object_or_404(Book,pk=pk)     
    book.delete()     
    messages.success(request,'Book deleted successfully')     
    return redirect('book_list')

@login_required
def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    ctx = {'book':book,'title':'Book Detail'}
    return render(request,'books/book_detail.html',context=ctx)

@login_required
def book_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box',None)       
        if search_query:
            books = Book.objects.filter(title__icontains=search_query).filter(status='a')       
            ctx = {'books':books,'title':'Book Search'}       
            return render(request,'books/book_search.html',context=ctx)       
        else:
            return redirect('book_list')       
    else:
        return redirect('book_list')

@login_required
def author_add(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'author added successfully')
            return redirect('author_view')
        else:
            messages.error(request, 'error adding author')
    ctx = {'form': form,'title': 'Add Author'}
    return render(request, 'books/add_author.html', ctx)

@login_required
def share_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == 'POST':
        form = BookShareForm(request.POST)
        if form.is_valid():
            share = form.save(commit=False)       
            share.user = request.user
            share.save()
            messages.success(request, 'Book shared successfully')
            return redirect('book_list',pk=book.pk)
        else:
            messages.error(request, 'Error sharing book')
    ctx = {'book':book,'form':BookShareForm()}
    return render(request, 'books/share_book.html', ctx)

@login_required
def share_delete(request,pk):            
    share = get_object_or_404(BookShare,pk=pk)     
    share.delete()     
    messages.success(request, 'Book Shared successfully')     
    return redirect('book_list',pk=share.book.pk)

@login_required
def share_detail(request,pk):
    share = get_object_or_404(BookShare,pk=pk)
    ctx = {'book':share.book,'title':'Book Detail'}
    return render(request,'books/book_detail.html',context=ctx)

@login_required
def share_list(request):
    shares = BookShare.objects.all()
    ctx = {'shares':shares,'title':'Book Share List'}
    return render(request,'books/book_share_list.html',context=ctx)





