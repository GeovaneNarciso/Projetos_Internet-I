from django.forms import ModelForm
from .models import *
from django import forms


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {'birth_date': forms.DateInput(attrs={'type': 'date', })}


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # widgets = {'authors': forms.Author.objects.filter(active=True)
