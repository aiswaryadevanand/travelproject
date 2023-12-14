from django.contrib import admin

# Register your models here.
from . models import place
from . models import people
admin.site.register(place)
admin.site.register(people)