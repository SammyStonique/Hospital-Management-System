# Generated by Django 4.2 on 2024-03-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients_registration', '0017_Removing_doctor_field_from_patient_history_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]