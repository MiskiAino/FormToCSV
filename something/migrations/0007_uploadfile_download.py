# Generated by Django 2.1.2 on 2018-11-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('something', '0006_document_urldownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='download',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
