# Generated by Django 3.2 on 2021-06-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='mobile_number',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]