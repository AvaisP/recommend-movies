from django.contrib import admin
from .models import User,Rating,Movie
# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)