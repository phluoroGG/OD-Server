# Generated by Django 4.2.4 on 2023-09-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_picturemodel_time_alter_picturemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemodel',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]