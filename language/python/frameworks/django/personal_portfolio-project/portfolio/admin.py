from django.contrib import admin

# Import the Project class
from .models import Project

# Register your models here to show up in admin page
admin.site.register(Project)