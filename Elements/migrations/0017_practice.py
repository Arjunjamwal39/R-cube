# Generated by Django 3.2.2 on 2022-05-16 04:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0016_alter_customer_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digits', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
