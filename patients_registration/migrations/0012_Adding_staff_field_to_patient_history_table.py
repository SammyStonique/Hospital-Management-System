# Generated by Django 4.2 on 2024-03-20 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients_registration', '0011_alter_patienthistory_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_to_visit', to=settings.AUTH_USER_MODEL),
        ),
    ]
