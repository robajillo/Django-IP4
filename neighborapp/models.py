from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Neighborhood(models.Model):
    name = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    profile_picture = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    