from django.shortcuts import render
from .models import Cat
# Create your views here.

from django.http import HttpResponse


def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {'cats': cats})


def about(request):
    return HttpResponse('<h1>About me page!</h1>')


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


cats = [
    Cat('Lolo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]
