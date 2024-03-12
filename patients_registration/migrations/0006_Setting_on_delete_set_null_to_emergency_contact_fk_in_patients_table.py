# Generated by Django 4.2 on 2024-03-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients_registration', '0005_Adding_patient_field_to_emergency_contacts_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='emergency_contact_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_contact_person', to='patients_registration.emergencycontactperson'),
        ),
    ]
