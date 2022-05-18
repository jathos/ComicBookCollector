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

class Reading(models.Model):
    date = models.DateField('Date Read')
    start_page = models.IntegerField()
    end_page = models.IntegerField()

    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_page}-{self.end_page}/{self.date}"

    class Meta:
        ordering = ['-date']