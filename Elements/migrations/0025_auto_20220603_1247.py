# Generated by Django 3.2.2 on 2022-06-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0024_auto_20220528_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('litre', 'litre'), ('unit', 'unit')], default='Nil', max_length=50),
        ),
        migrations.AlterField(
            model_name='deliveryboy',
            name='stat',
            field=models.CharField(choices=[('took off', 'took off'), ('free', 'free'), ('duty', 'duty')], default='duty', max_length=50),
        ),
    ]
