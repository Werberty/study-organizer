# Generated by Django 4.1.3 on 2022-12-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0025_alter_historic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historic',
            name='date',
            field=models.DateField(),
        ),
    ]