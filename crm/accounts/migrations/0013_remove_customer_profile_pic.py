# Generated by Django 3.2.8 on 2022-06-19 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
