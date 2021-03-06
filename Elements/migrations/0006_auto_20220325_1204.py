# Generated by Django 3.2.2 on 2022-03-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0005_auto_20220324_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('discription', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('image', models.ImageField(upload_to='static/card_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
