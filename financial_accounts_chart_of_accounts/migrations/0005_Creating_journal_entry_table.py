# Generated by Django 4.2 on 2024-03-21 17:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_Creating_company_table'),
        ('financial_accounts_chart_of_accounts', '0004_Creating_journals_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('journal_entry_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField()),
                ('debit_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('credit_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_journal_entry', to='company.company')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entryy', to='financial_accounts_chart_of_accounts.journal')),
                ('posting_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entry_posting_account', to='financial_accounts_chart_of_accounts.ledger')),
            ],
            options={
                'ordering': ['-date', 'journal'],
            },
        ),
    ]