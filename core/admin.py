from django.contrib import admin
from .models import Farmer, Land, Crop

admin.site.register(Farmer)
admin.site.register(Land)
admin.site.register(Crop)