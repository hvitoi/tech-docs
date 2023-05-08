from django.db import models

# Models are classes! And tables for the database

class Project(models.Model):        # Django model types   
    title = models.CharField(max_length=100)      # Setup options     
    description = models.CharField(max_length=200)    
    image = models.ImageField(upload_to='portfolio/images')   
    url = models.URLField(blank=True)   