# Generated by Django 3.2.2 on 2022-05-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0014_rename_number_customer_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Contact_number',
            field=models.IntegerField(),
        ),
    ]
