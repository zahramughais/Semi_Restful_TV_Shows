from xmlrpc.client import DateTime
from django.db import models
from datetime import datetime
class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData.get('title', [])) < 2:
            errors['title'] = "Movie title should be at least 2 characters"
        if len(postData.get('network', [])) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData.get('desc', [])) > 0 and len(postData.get('desc', [])) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        return errors
class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField(default="no description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager()