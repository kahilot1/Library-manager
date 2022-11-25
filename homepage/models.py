from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False)
    id = models.CharField(max_length=100, primary_key=True)
    book_owner = models.CharField(max_length=100)
    def __str__(self):
        return self.title