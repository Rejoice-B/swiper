# Generated by Django 4.1.7 on 2023-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_avatar_alter_user_birth_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vip_id',
            field=models.IntegerField(default=1, verbose_name='Vip ID'),
        ),
    ]
