from signal import signal
from django.db import models
from resumepage.settings import MEDIA_ROOT
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    duration = models.CharField(max_length=45)
    course = models.CharField(max_length=45)
    university = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    description = models.TextField()

    def __str__(self):
        return self.course

class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    duration = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.TextField()
    programming_language = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Skill(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    description = models.TextField()
    certificate = models.FileField(max_length=455)

    def __str__(self):
        return self.name

def post_user_created(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created, sender=User)