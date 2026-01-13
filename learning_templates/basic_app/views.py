from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'basic_app/home.html',)

def book(request):
    return render(request,'basic_app/book.html',)

def about(request):
    return render(request,'basic_app/about.html',)