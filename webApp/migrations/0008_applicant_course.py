# Generated by Django 5.1 on 2024-08-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_remove_applicant_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='course',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
