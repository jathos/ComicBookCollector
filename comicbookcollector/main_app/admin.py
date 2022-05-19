from django.contrib import admin
from .models import Comic, Reading, Artist, Photo

# Register your models here.
admin.site.register(Comic)
admin.site.register(Reading)
admin.site.register(Artist)
admin.site.register(Photo)