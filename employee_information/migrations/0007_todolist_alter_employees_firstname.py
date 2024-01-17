# Generated by Django 4.2.3 on 2024-01-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0006_employees_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('duration', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='firstname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
