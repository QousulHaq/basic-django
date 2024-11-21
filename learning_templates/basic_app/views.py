from django.shortcuts import render

# Create your views here.

def index (request) :
    index_context = {'name': "hello world!", 'number' : 100 }
    return render(request, 'basic_app/index.html', context=index_context)

def profile (request) :
    return render(request, 'basic_app/profile.html')

def contact (request) :
    return render(request, 'basic_app/contact.html')
