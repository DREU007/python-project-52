# Generated by Django 4.2.6 on 2023-11-19 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('label', '0003_remove_label_task'),
        ('task', '0002_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, error_messages={'unique': 'Task status with such Name already exist.'}, help_text='Required 255 characters or fewer.', max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, to='label.label'),
        ),
    ]
