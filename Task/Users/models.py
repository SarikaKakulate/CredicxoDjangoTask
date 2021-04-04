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
    user_level   = models.CharField(_('User Level'), choices=USER_LEVEL_CHOICES, blank=False, null=False, max_length=50)
   
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Student(models.Model):
    
    first_name      = models.CharField(_("First Name"), blank=False, null=False, max_length=255)
    last_name       = models.CharField(_("Last Name"), blank=False, null=False, max_length=255)
    student_class   = models.CharField(_("Student Class"), blank=False, null=False, max_length=255)
    student_roll    = models.CharField(_("Student Roll"), blank=False, null=False, max_length=255)
    
    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    
    first_name      = models.CharField(_("First Name"), blank=False, null=False, max_length=255)
    last_name       = models.CharField(_("Last Name"), blank=False, null=False, max_length=255)
    
    def __str__(self):
        return self.first_name

