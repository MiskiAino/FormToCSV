# Generated by Django 2.1.2 on 2018-11-29 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('something', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='something.Document'),
        ),
    ]
