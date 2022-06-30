from django.contrib import admin
from .models import Client, Agent, User
# Register your models here.

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Client)