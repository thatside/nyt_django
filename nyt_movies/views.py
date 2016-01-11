from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    context = {
        'message': 'I love you, my dear',
    }
    return render(request, 'nyt_movies/index.html', context=context)

