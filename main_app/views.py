from django.shortcuts import render
from django.http import HttpResponse
from .models import Links
import uuid
# Create your views here.


def index(request):
    links = Links.objects.all()
    return render(request, 'index.html', {'links': links})

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_link = Links(full_link=link,short_link=uid)
        new_link.save()
        links = Links.objects.all()
        print(links)
        return render(request, 'index.html', {'links': links})