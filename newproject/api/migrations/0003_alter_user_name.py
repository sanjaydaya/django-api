# Generated by Django 5.1.2 on 2024-11-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
