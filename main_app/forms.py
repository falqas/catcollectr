# main_app/forms.py
from django import forms


class CatForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    breed = forms.CharField(label='Breed', max_length=100)
    description = forms.CharField(label='Description', max_length=250)
    age = forms.IntegerField(label='Age')
