# Generated by Django 4.2.3 on 2023-07-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.CharField(max_length=100)),
                ('items_bought', models.IntegerField()),
                ('active', models.BooleanField()),
                ('date', models.DateField()),
            ],
        ),
    ]