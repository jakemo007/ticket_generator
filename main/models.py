from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Tickets(models.Model):
    name = models.CharField(max_length=255,default=None)
    description = models.TextField(default=None)
    author  = models.ForeignKey(User,models.CASCADE)
    is_updated_by_admin = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:homepage')

