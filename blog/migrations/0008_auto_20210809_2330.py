# Generated by Django 2.2.4 on 2021-08-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210809_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cod',
            name='check_image',
            field=models.ImageField(upload_to='media/target'),
        ),
    ]