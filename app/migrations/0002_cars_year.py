# Generated by Django 4.2.14 on 2024-07-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='year',
            field=models.TextField(max_length=4, null=True),
        ),
    ]
