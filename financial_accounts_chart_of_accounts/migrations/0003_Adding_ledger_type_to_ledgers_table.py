# Generated by Django 4.2 on 2024-03-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_accounts_chart_of_accounts', '0002_Adding_financial_statement_field_to_ledgers_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='ledger_type',
            field=models.CharField(choices=[('', 'Select Ledger Type'), ('Cashbook', 'Cashbook'), ('Current Asset', 'Current Asset'), ('Fixed Asset', 'Fixed Asset'), ('Current Liability', 'Current Liability'), ('Longterm Liability', 'Longterm Liability'), ('Owner Equity', 'Owner Equity'), ('Income', 'Income'), ('Expenses', 'Expenses')], default='', max_length=250),
        ),
    ]
