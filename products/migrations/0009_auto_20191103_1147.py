# Generated by Django 2.2.2 on 2019-11-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191103_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default='default-image.jpg', upload_to='products/images/'),
        ),
    ]