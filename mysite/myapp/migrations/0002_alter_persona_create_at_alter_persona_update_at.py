# Generated by Django 4.1.3 on 2022-11-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='create_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='update_at',
            field=models.DateTimeField(),
        ),
    ]