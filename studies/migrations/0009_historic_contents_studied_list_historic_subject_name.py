# Generated by Django 4.1.3 on 2023-05-03 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0008_alter_historic_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='historic',
            name='contents_studied_list',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historic',
            name='subject_name',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]