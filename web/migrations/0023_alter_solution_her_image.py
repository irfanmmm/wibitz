# Generated by Django 4.2.5 on 2023-10-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_solution_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='her_image',
            field=models.ImageField(upload_to='testimonials/'),
        ),
    ]
