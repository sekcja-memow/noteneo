# Generated by Django 3.1.4 on 2020-12-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201201_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]