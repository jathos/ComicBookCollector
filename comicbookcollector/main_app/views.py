import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Comic, Artist, Photo
from .forms import ReadingForm

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
  artists_comic_doesnt_have = Artist.objects.exclude(id__in = comic.artists.all().values_list('id'))
  reading_form = ReadingForm()
  return render(request, 'comics/detail.html', { 'comic' : comic, 'reading_form' : reading_form, 'artists': artists_comic_doesnt_have })  

def add_reading(request, comic_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.comic_id = comic_id
        new_reading.save()
    return redirect ('details', comic_id = comic_id)

def assoc_artist(request, comic_id, artist_id):
    Comic.objects.get(id=comic_id).artists.add(artist_id)
    return redirect('details', comic_id=comic_id)

class ComicCreate(CreateView):
    model = Comic
    fields = ['series', 'title', 'publisher', 'issue_num', 'year']

    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

def add_photo(request, comic_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, comic_id=comic_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', comic_id=comic_id)

class ComicUpdate(UpdateView):
    model = Comic
    fields = ['title']

    success_url = '/comics'

class ComicDelete(DeleteView):
    model = Comic
    success_url = '/comics'