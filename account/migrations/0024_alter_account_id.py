# Generated by Django 3.2.9 on 2021-12-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]