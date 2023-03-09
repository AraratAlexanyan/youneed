from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import FileExtensionValidator
from django.db import models

from user_profile.services.image_service import get_avatar_path, validate_image_size
from user_profile.user_manager import UserManager


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    bio = models.TextField(max_length=2048, blank=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=50, null=True, blank=True, unique=True)
    avatar = models.ImageField(default='default.jpg',
                               upload_to=get_avatar_path,
                               validators=[FileExtensionValidator(
                                    allowed_extensions=['jpg', 'jpeg', 'bmp']),
                                    validate_image_size])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    github_link = models.URLField(max_length=256, blank=True, null=True)
    linkedin_link = models.URLField(max_length=256, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.first_name
