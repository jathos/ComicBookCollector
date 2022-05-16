from django.shortcuts import render
from django.http import HttpResponse
from .models import Comic

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    comic_data = Comic.objects.all()
    return render(request, 'comics/index.html', { 'comic_data' : comic_data })

def comic_details(request, comic_id):
  comic = Comic.objects.get(id=comic_id)
  return render(request, 'comics/detail.html', { 'comic' : comic })  
