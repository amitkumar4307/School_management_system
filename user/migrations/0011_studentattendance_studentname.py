# Generated by Django 5.0.6 on 2024-07-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_studentattendance_sclass_alter_student_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattendance',
            name='studentname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
