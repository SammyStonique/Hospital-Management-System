# Generated by Django 4.2 on 2024-03-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts_chart_of_accounts', '0007_Additional_fields_to_journal_entries_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='reference_no',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]