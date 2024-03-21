# Generated by Django 4.2 on 2024-03-20 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients_registration', '0009_Adding_gender_field_to_patients_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patienthistory',
            options={'ordering': ['-date', 'patient']},
        ),
        migrations.AlterField(
            model_name='patientfollowuphistory',
            name='patient_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_history_followup', to='patients_registration.patienthistory'),
        ),
    ]