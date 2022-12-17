from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class Links(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    link_belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)


class Socials(models.Model):
    social_media_name = models.CharField(max_length=255)
    profile_link = models.CharField(max_length=255)
    profile_belongs_to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

