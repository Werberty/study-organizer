# Generated by Django 4.1.3 on 2022-12-20 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0026_alter_historic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
