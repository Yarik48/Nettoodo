# Generated by Django 4.1.7 on 2023-03-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='days',
            name='weekend',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
