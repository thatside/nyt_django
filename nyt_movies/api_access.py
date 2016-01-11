import requests

__api_key = '39f5e7078c663303fae980eed9401a52:5:73985898'


def get_picks(offset=0, order='by-publication-date', resource_type='all'):
    base_url = 'http://api.nytimes.com/svc/movies/v2/reviews/' + resource_type + '/'
    params = {
        'api-key': __api_key,
        'offset': offset,
        'order': order,
    }
    r = requests.get(base_url, params=params)

    return r.json()['results']



