# Generated by Django 4.0.3 on 2022-04-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_resume_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(upload_to='resume'),
        ),
    ]
