from django.contrib import admin

# Register your models here.
from .models import Vaksin, Pendaftar

admin.site.register(Vaksin)
admin.site.register(Pendaftar)