# Generated by Django 4.1.1 on 2022-09-15 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
