# Generated by Django 4.2 on 2024-03-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts_chart_of_accounts', '0016_alter_journal_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='banking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]