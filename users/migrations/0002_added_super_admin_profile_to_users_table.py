# Generated by Django 4.2 on 2024-02-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_creating_a_custom_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.CharField(blank=True, choices=[('', 'Select User Profile'), ('Super Admin', 'Super Admin'), ('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Patient', 'Patient'), ('Accountant', 'Accountant'), ('Human Resource', 'Human Resource'), ('Nurse', 'Nurse'), ('Lab Technician', 'Lab Technician'), ('Office Clerk', 'Office Clerk'), ('Clinical Officer', 'Clinical Officer')], default='', max_length=250),
        ),
    ]