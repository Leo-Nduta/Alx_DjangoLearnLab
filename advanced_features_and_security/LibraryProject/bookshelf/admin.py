from django.contrib import admin
from .models import Book

#Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author'  'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register your models here.
admin.site.register(Book)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
