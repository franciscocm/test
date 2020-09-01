from django.contrib import admin
from .models import clients, catalog, backlog

# Register your models here.

admin.site.register(clients)
admin.site.register(catalog)
admin.site.register(backlog)