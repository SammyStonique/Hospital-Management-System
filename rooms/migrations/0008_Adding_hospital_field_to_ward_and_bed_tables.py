# Generated by Django 4.2 on 2024-03-15 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_Creating_company_table'),
        ('rooms', '0007_Creating_a_beds__table'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='hospital',
            field=models.ForeignKey(default='9e14bcef-d3c1-400c-a8c0-66d7b25cc5ff', on_delete=django.db.models.deletion.CASCADE, related_name='hospital_bed', to='company.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='hospital',
            field=models.ForeignKey(default='9e14bcef-d3c1-400c-a8c0-66d7b25cc5ff', on_delete=django.db.models.deletion.CASCADE, related_name='hospital_ward', to='company.company'),
            preserve_default=False,
        ),
    ]
