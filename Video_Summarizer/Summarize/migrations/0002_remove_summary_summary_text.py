# Generated by Django 4.2 on 2023-05-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Summarize', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='summary_text',
        ),
    ]