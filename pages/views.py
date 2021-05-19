from django.shortcuts import render
from . import models
import re
from urllib.parse import unquote
import requests
from django.views.decorators.csrf import csrf_exempt
import pyshorteners


s = pyshorteners.Shortener()
print(s.tinyurl.short('https://python-scripts.com/f-strings'))


def valid_url(url):
    if requests.get(url).status_code == 200:
        return True
    return False


@csrf_exempt
def main(request):
    try:
        method = request.method
        if method == "GET":
            url = request.GET.get('url', 0)
        elif method == "POST":
            print(request.POST)
            url = request.POST.get('url', 0)
        elif method == "PUT":
            url = unquote(re.findall(r'url=(.+)', request.body.decode())[0])
        else:
            url = unquote(re.findall(r'url=(.+)', request.body.decode())[0])
        if valid_url(url):
            if method == 'DELETE':
                models.url_table.objects.get(url=url).delete()
                return render(request, 'main.html', {'text': 'url_deleted_from_db'})
            else:
                if url in [obj.url for obj in models.url_table.objects.all()]:
                    shorten_url = models.url_table.objects.get(url=url).shorten_url
                else:
                    shorten_url = s.tinyurl.short(url)
                    models.url_table.objects.get_or_create(shorten_url=shorten_url, url=url)
                return render(request, 'main.html', {'text': 'shorten url:', 'url': shorten_url})
        return render(request, 'main.html', {'text': 'invalid_url'})
    except requests.exceptions.MissingSchema:
        return render(request, 'main.html', {'text': 'invalid_url'})
