from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    profile_picture = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    