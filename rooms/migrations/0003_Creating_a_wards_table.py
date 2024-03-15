# Generated by Django 4.2 on 2024-03-14 17:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_Adding_company_field_to_rooms_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(choices=[('', 'Select Category'), ('Children', 'Children'), ('Women', 'Women'), ('Men', 'Men')], default='', max_length=250)),
                ('wing', models.CharField(blank=True, max_length=250, null=True)),
                ('ward_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='patient',
        ),
    ]