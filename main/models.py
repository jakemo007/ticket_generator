from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.


class Tickets(models.Model):
    name = models.CharField(max_length=255,default=None)
    description = models.TextField(default=None)
    author  = models.ForeignKey(User,models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:homepage')

@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    pass