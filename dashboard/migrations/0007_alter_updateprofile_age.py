# Generated by Django 3.2.3 on 2021-12-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_updateprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateprofile',
            name='age',
            field=models.CharField(max_length=2),
        ),
    ]
