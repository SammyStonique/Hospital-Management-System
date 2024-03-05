# Generated by Django 4.2 on 2024-03-01 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xtra', '0001_Creating_department_table'),
        ('users', '0002_Adding_allowed_company_and_image_fields_to_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='department',
            field=models.ForeignKey(default='5a172345-3749-4942-972d-f7a0b7c44561', on_delete=django.db.models.deletion.CASCADE, related_name='dep_manager', to='xtra.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_department',
            field=models.ForeignKey(default='5a172345-3749-4942-972d-f7a0b7c44561', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_departments', to='xtra.department'),
            preserve_default=False,
        ),
    ]