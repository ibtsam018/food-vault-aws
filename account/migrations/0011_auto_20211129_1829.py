# Generated by Django 3.1.1 on 2021-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20211129_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='/profilepic/useravatar.png', upload_to='D:\\react_blog\\blog_django\\core\\media/profilepic'),
        ),
    ]