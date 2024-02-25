from django.db import models

# Create your models here.

class Department(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name} Department'
    
    class Meta:
        ordering = [('id')]