from django.db import models

# Create your models here.
class Comic(models.Model):
    series = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    issue_num = models.IntegerField()
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title