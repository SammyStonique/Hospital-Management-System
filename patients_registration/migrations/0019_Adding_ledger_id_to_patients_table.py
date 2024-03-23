# Generated by Django 4.2 on 2024-03-22 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts_chart_of_accounts', '0012_Adding_ledger_id_to_patients_table'),
        ('patients_registration', '0018_Checking_if_staff_is_doctor_field_patient_history_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ledger_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='financial_accounts_chart_of_accounts.ledger'),
        ),
    ]
