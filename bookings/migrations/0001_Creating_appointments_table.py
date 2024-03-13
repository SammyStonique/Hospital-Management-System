# Generated by Django 4.2 on 2024-03-12 07:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients_registration', '0006_Setting_on_delete_set_null_to_emergency_contact_fk_in_patients_table'),
        ('company', '0001_Creating_company_table'),
        ('doctor_profile', '0003_Creating_doctor_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_appointment', to='doctor_profile.doctor')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_hospital', to='company.company')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to='patients_registration.patient')),
            ],
        ),
    ]
