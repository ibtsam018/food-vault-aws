# Generated by Django 3.1.1 on 2021-11-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='/profilepic/useravatar.png', upload_to='media/profilepic'),
        ),
    ]