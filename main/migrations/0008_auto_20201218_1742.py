# Generated by Django 2.2.6 on 2020-12-18 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201218_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transiction',
            name='typeof',
        ),
        migrations.DeleteModel(
            name='MoneyType',
        ),
    ]