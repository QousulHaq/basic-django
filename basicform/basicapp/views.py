from django.shortcuts import render
from . import form

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    forms = form.FormName()

    if request.method == "POST":
        forms = form.FormName(request.POST)

        if forms.is_valid():
            print("validation success")
            print(forms.cleaned_data['name'])
            print(forms.cleaned_data['email'])
            print(forms.cleaned_data['text'])


    return render(request, 'basicapp/form_page.html', {'form' : forms})
