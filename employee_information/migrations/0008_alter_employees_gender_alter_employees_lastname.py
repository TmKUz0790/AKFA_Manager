# Generated by Django 4.2.3 on 2024-01-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0007_todolist_alter_employees_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='gender',
            field=models.CharField(blank=True, default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees',
            name='lastname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]