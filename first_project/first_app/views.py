from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord

# Create your views here.

def index(request):
    webpage = AccessRecord.objects.order_by("date")

    data = {
        "content" : "hello world",
        "title" : "nyoba template",
        "webpage" : webpage,
    }
    
    return render(request, 'first_app/index.html', context=data)
