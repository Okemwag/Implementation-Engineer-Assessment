from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'year', 'created_at')
    list_filter = ('year', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-year', 'title')
    
admin.site.register(Movie, MovieAdmin)