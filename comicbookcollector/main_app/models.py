from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('artists_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

class Comic(models.Model):
    series = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    issue_num = models.IntegerField()
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    artists = models.ManyToManyField(Artist)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    url = models.CharField(max_length=200)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.comic_id}"


class Reading(models.Model):
    date = models.DateField('Date Read')
    start_page = models.IntegerField()
    end_page = models.IntegerField()

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_page}-{self.end_page}/{self.date}"

    class Meta:
        ordering = ['-date']

