from django.shortcuts import render
from .models import Cat
from .forms import CatForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse


def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats': cats, 'form': form})


def about(request):
    return HttpResponse('<h1>About me page!</h1>')


def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})


def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid():
        cat = form.save(commit=False)
        # Add this line...
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect('/')


def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4)
# ]
