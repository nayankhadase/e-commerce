# Generated by Django 3.2 on 2021-06-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='address',
            field=models.CharField(default='none', max_length=300),
        ),
        migrations.AddField(
            model_name='userdata',
            name='mobile_number',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='userdata',
            name='user_status',
            field=models.CharField(choices=[('BLOCK', 'Block'), ('UNBLOCK', 'Unblock')], default='BLOCK', max_length=20),
        ),
    ]
