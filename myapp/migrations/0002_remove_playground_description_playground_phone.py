# Generated by Django 5.1.5 on 2025-02-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playground',
            name='description',
        ),
        migrations.AddField(
            model_name='playground',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
