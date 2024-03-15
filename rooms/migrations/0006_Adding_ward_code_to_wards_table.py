# Generated by Django 4.2 on 2024-03-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_Adding_department_name_to_rooms_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='department_name',
        ),
        migrations.AddField(
            model_name='ward',
            name='ward_code',
            field=models.CharField(default='ABC', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
