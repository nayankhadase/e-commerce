# Generated by Django 3.2 on 2021-06-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0)),
                ('uid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.TextField(default='none'),
        ),
    ]
