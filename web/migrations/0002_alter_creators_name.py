# Generated by Django 4.2.5 on 2023-10-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creators',
            name='name',
            field=models.CharField(default=True, max_length=100, null=True),
        ),
    ]