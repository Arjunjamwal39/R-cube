# Generated by Django 3.2.2 on 2022-03-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elements', '0007_auto_20220325_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crousal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('discription', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='crousal_imgages')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('E', 'Eatables'), ('C', 'Clothing'), ('F', 'Furniture'), ('H', 'Home_decor'), ('L', 'Latest')], default='', max_length=2),
        ),
    ]
