from django.contrib import admin
from django.contrib.auth.models import Group
from . models import gallery



# Register your models here.
admin.site.site_header = "ProjectMaterials Admin Dashboard"

admin.site.register(gallery)