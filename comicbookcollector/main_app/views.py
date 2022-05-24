import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Comic, Artist, Photo
from .forms import ReadingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def comics_index(request):
    comic_data = Comic.objects.filter(user=request.user)
    return render(request, 'comics/index.html', { 'comic_data' : comic_data })

@login_required
def comic_details(request, comic_id):
  comic = Comic.objects.get(id=comic_id)
  artists_comic_doesnt_have = Artist.objects.exclude(id__in = comic.artists.all().values_list('id'))
  reading_form = ReadingForm()
  return render(request, 'comics/detail.html', { 'comic' : comic, 'reading_form' : reading_form, 'artists': artists_comic_doesnt_have })  

@login_required
def add_reading(request, comic_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.comic_id = comic_id
        new_reading.save()
    return redirect ('details', comic_id = comic_id)

@login_required
def assoc_artist(request, comic_id, artist_id):
    Comic.objects.get(id=comic_id).artists.add(artist_id)
    return redirect('details', comic_id=comic_id)

class ComicCreate(LoginRequiredMixin, CreateView):
    model = Comic
    fields = ['series', 'title', 'publisher', 'issue_num', 'year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('details', args=(self.object.id,))

@login_required
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

class ComicUpdate(LoginRequiredMixin, UpdateView):
    model = Comic
    fields = ['title']

    success_url = '/comics'

class ComicDelete(LoginRequiredMixin, DeleteView):
    model = Comic
    success_url = '/comics'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)