# Generated by Django 4.2 on 2024-03-21 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients_registration', '0014_Removing_patient_history_id_from_other_tables'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientHistory',
        ),
    ]
