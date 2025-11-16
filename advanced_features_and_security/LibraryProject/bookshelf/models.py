from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.publication_year}"

from django.contrib.auth.models import AbstractUser, BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and save a regular user with required username, email, and password.
        """
        if not username:
            raise ValueError("The username must be set")
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)  # hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and save a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=False, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Meta:
        permissions = [
            ("can_view", "Can view user profile"),
            ("can_create", "Can create user profile"),
            ("can_edit", "Can edit user profile"),
            ("can_delete", "Can delete user profile"),
        ]