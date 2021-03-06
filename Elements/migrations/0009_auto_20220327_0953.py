# Generated by Django 3.2.2 on 2022-03-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0008_auto_20220326_1537'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Crousal',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'Eatables'), ('C', 'Clothing'), ('F', 'Furniture'), ('H', 'Home_decor'), ('L', 'Latest'), ('S', 'Slider')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]
