# Generated by Django 5.1.2 on 2024-10-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_empuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
    ]