# Generated by Django 3.2 on 2021-04-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
