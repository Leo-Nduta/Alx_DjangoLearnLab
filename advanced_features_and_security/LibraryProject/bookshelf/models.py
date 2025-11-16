from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.publication_year}"

from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('date_of_birth', None)
        extra_fields.setdefault('profile_photo', None)
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self().create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=False, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
