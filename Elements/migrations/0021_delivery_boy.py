# Generated by Django 3.2.2 on 2022-05-28 06:13

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0020_userotp'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery_boy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('discription', models.TextField(null=True)),
            ],
        ),
    ]
