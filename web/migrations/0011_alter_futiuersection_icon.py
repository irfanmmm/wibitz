# Generated by Django 4.2.5 on 2023-10-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_futiuersection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futiuersection',
            name='icon',
            field=models.FileField(upload_to='testimonials/'),
        ),
    ]
