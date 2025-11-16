from django.contrib import admin
from .models import Book

#Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author'  'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register your models here.
admin.site.register(Book)