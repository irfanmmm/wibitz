# Generated by Django 4.2.5 on 2023-10-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_creators_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creators',
            name='image',
            field=models.FileField(upload_to='testimonials/'),
        ),
    ]
