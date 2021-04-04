from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):

    USER_LEVEL_CHOICES = (
      ('student', 'student'),
      ('teacher', 'teacher'),
    )
    
    username     = models.CharField(_("Username"), blank=False, null=False, max_length=255, unique=True)
    first_name   = models.CharField(_("First Name"), blank=False, null=False, max_length=255)
    last_name    = models.CharField(_("Last Name"), blank=False, null=False, max_length=255)
    email        = models.EmailField(_('Email'), blank=False, null=False, unique=True)
    user_level   = models.CharField(_('User Level'), choices=USER_LEVEL_CHOICES)
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

