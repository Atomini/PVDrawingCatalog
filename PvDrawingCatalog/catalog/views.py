from django.shortcuts import render
from .models import Book, AssemblyDrawing


# Create your views here.

def show_book_tree(request):
    return render(request, 'book.html', {'book': Book.objects.all()})


def show_assembly_tree(request):
    return render(request, 'assembly.html', {'assembly': AssemblyDrawing.objects.all()})
