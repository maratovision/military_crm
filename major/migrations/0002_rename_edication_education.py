# Generated by Django 3.2 on 2021-05-05 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_dossier_image'),
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Edication',
            new_name='Education',
        ),
    ]