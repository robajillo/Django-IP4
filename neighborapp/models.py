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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, related_name='members', blank=True)
    profile_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.user.username} profile'