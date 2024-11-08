from django import forms
from django.core import validators

def check_for_a(value): # validasi custom sesuai keinginan
    if value[0].lower() != "a":
        raise forms.ValidationError("Harus berawalan huruf A coy")

class FormName(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5)]) #validasi dengan library validator
    email = forms.EmailField()
    verify_email = forms.EmailField(label="masukkan email anda lagi")
    text = forms.CharField(widget=forms.Textarea, validators=[check_for_a])

    def clean(self): #validasi dari dua inputan, apakah sama?
        all_clean_data =super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Email haru sama cyakk!")