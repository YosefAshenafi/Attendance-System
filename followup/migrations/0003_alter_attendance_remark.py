# Generated by Django 4.1.4 on 2023-07-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0002_rename_was_avilable_attendance_was_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='remark',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]