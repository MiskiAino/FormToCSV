# Generated by Django 2.1.2 on 2018-11-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('something', '0008_auto_20181130_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='upload',
            field=models.FileField(upload_to=''),
        ),
    ]
