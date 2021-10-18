# Generated by Django 3.2.8 on 2021-10-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='product_size',
            options={'verbose_name': 'Product_size', 'verbose_name_plural': 'Product_size'},
        ),
        migrations.AddField(
            model_name='product',
            name='product_photo_5',
            field=models.ImageField(default='image', upload_to='Product/%Y/%M/'),
            preserve_default=False,
        ),
    ]
