# Generated by Django 4.2.5 on 2023-10-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_marketting_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('button_color', models.CharField(max_length=250)),
                ('backgroun', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='testimonials/')),
            ],
        ),
    ]
