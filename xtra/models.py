from django.db import models
from company.models import Company
import uuid


# Create your models here.

class Department(models.Model):
    department_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    code = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company, related_name="company_dep", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Department'
    
    class Meta:
        ordering = [('name')]
