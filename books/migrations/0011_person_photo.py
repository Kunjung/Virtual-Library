# Generated by Django 2.2 on 2019-04-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20190417_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
