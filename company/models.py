from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    company_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=250)
    town = models.CharField(max_length=250)
    logo = models.ImageField(default='default_logo.png', upload_to='company_pics')
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    kra_pin = models.CharField(max_length=250)
    registration_number = models.CharField(max_length=250)
    country = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = [('name')]
