# Generated by Django 4.0.2 on 2022-02-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]