# Generated by Django 2.2.5 on 2019-09-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190912_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='session',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('B', 'Beer:30')], default='M', max_length=1),
        ),
    ]
