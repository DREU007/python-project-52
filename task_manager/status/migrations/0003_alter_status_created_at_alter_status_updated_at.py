# Generated by Django 4.2.6 on 2023-11-13 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_status_created_at_status_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
