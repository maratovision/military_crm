# Generated by Django 3.2 on 2021-04-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='date_expired',
            field=models.DateField(),
        ),
    ]
