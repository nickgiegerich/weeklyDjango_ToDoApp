# Generated by Django 3.0.4 on 2020-03-25 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20200323_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskline',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
