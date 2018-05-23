# main_app/forms.py
from django import forms

# Add this line...
from .models import Cat
# Change the line below to use ModelForm...


class CatForm(forms.ModelForm):
    # # Replace the contents with these lines...
    # name = forms.CharField(label='Name', max_length=100)
    # breed = forms.CharField(label='Breed', max_length=100)
    # description = forms.CharField(label='Description', max_length=250)
    # age = forms.IntegerField(label='Age')

    # Give your model metadata by using an inner class Meta. Model metadata is “anything that’s not a field”,
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'description', 'age']
