from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Tickets)
admin.site.site_header = 'Ticket Admin'