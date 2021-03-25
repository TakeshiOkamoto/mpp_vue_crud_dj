from django.contrib import admin

# Register your models here.
from .models import VueCrudData, VueCrudDataBk
admin.site.register(VueCrudData)
admin.site.register(VueCrudDataBk)