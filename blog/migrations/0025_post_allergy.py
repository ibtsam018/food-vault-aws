# Generated by Django 3.1.1 on 2021-11-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20211002_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='allergy',
            field=models.TextField(null=True),
        ),
    ]
