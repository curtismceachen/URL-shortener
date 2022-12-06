from django.shortcuts import render
from .models import Links
import uuid
# Create your views here.


def index(request):
    links = Links.objects.all()
    return render(request, 'index.html', {'links': links})

def create(request):
    if request.method == 'POST':
        # create an object with the html input as the full link, and a random set of chars as the short link
        # uuid4 returns a very long string of random chars, shorten it to 5 characters with [:5]
        new_link = Links(full_link=request.POST['link'], short_link=str(uuid.uuid4())[:5])
        new_link.save()
        links = Links.objects.all()
        return render(request, 'index.html', {'links': links})

def search(request):
    if request.method == 'POST':
        try:
            search_result = Links.objects.get(short_link=request.POST['shortened_link'])
        except Links.DoesNotExist:
            search_result = 'There are no records for that short link.'
        links = Links.objects.all()
        return render(request, 'index.html', {'links': links, 'search_result': search_result})
