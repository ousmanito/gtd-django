# Generated by Django 4.0.4 on 2022-05-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0012_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
