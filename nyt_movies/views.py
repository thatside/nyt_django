from django.shortcuts import render
import pprint
from . import api_access


def index(request):
    results = api_access.get_picks()
    picks = []
    for item in results:
        picks.append({'name': item['display_title']})
    context = {
        'message': 'I love you, my dear',
        'results': picks
    }
    return render(request, 'nyt_movies/index.html', context=context)

