from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("You didn't provide invalid email address")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,**extra_fields)