# Generated by Django 4.2 on 2024-03-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts_chart_of_accounts', '0008_Adding_reference_number_field_to_journals_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='banking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
