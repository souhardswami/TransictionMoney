# Generated by Django 2.2.6 on 2020-12-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201215_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='targetuser',
            field=models.CharField(default='', max_length=10),
        ),
    ]