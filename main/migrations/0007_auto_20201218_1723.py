# Generated by Django 2.2.6 on 2020-12-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_customuser_targetuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='targetuser',
            field=models.CharField(default='0000000000', max_length=10),
        ),
    ]