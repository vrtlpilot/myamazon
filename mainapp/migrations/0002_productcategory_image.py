# Generated by Django 2.0.3 on 2018-03-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images', verbose_name='Изображение'),
        ),
    ]