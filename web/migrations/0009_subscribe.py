# Generated by Django 4.2.5 on 2023-10-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_image_creators_files_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]