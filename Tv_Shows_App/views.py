from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from .models import *

def root(request):
    return redirect("/shows")

def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request ,"index.html", context)

def create_new(request):
    return render(request, "create.html")

def add_new(request):
    if request.method == 'POST':
        newMovie = Movie.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['rel_date'],
            desc=request.POST['desc'],
        )
        newMovie.save()
    return redirect("Display", id = newMovie.id)

def dis_show(request, id):
    context = {
        'movie': Movie.objects.get(id = id),
    }
    return render(request, 'show.html', context)

def edit_show(request,id):
    context = {
        'movie': Movie.objects.get(id=id),
    }
    return render(request, "edit.html", context)

def update_show(request, id):
    if request.method == 'POST':
        update_movie = Movie.objects.get(id=id)
        update_movie.title= request.POST['title']
        update_movie.network= request.POST['network']
        update_movie.release_date= request.POST['rel_date']
        update_movie.desc= request.POST['desc']
        update_movie.save()
    return redirect("Display", id = update_movie.id)

def del_show(request, id):
    movie_to_del = Movie.objects.get(id=id)
    movie_to_del.delete()
    return redirect("/shows")