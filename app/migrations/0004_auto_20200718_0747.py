# Generated by Django 2.2 on 2020-07-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200718_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
