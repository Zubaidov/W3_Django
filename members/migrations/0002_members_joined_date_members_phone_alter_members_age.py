# Generated by Django 5.0 on 2023-12-09 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]