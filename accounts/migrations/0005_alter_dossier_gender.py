# Generated by Django 3.2 on 2021-04-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]