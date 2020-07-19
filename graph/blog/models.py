from django.db import models

# Create your models here.
class Todoitem(models.Model):
    content=models.TextField()
    
