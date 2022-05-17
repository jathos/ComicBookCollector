from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
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

class ComicCreate(CreateView):
    model = Comic
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

class ComicUpdate(UpdateView):
    model = Comic
    fields = ['title']

    success_url = '/comics'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics'