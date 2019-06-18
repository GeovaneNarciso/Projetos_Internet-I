from django.shortcuts import render, redirect
from .forms import *


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


def add_book(request):
    authors = Author.objects.filter(active=True)
    # authors = Author.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.save()
            form.save_m2m()
            return redirect('list_books')
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form, 'authors': authors})
