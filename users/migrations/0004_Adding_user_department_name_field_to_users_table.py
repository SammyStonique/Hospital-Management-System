# Generated by Django 4.2 on 2024-03-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_Adding_department_field_to_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_department_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]