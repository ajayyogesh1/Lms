# Generated by Django 2.2.12 on 2020-05-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Password',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='PhoneNumber',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
