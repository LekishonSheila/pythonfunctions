# Generated by Django 4.2.3 on 2023-08-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.IntegerField(),
        ),
    ]
