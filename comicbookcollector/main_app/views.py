from django.shortcuts import render
from django.http import HttpResponse

class Comic:  # Note that parens are optional if not inheriting from another class
  def __init__(self, series, title, issue_num, publisher, year):
    self.series = series
    self.title = title
    self.issue_num = issue_num
    self.publisher = publisher
    self.year = year

comic = [
  Comic('Superman', 'The Day Superman Ate Gluten', '100', 'DC', '1995'),
  Comic('Transformers', 'Return of the Decepticons', '24', 'Marvel', '1989'),
  Comic('Teenage Mutant Ninja Turtles', 'The Secret of the Ooze', '5', 'Archie', '1991')
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def comics_index(request):
    return render(request, 'comics/index.html', { 'comics': comic })
