from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Neighborhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    health = models.IntegerField( default=0)
    police = models.IntegerField( default=0)
    
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    email = models.EmailField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name

    def create_business(self):
        self.save

    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post')

    