# Generated by Django 4.2.3 on 2023-08-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('catagory', models.CharField(choices=[('sn', 'Sneakers'), ('lf', 'Loafer'), ('bs', 'Brogue shoe'), ('sp', 'sport')], max_length=5)),
                ('color', models.CharField(choices=[('re', 'red'), ('ye', 'yellow'), ('bl', 'black'), ('wh', 'white'), ('bl', 'blue')], max_length=5)),
                ('product_images', models.ImageField(upload_to='product')),
            ],
        ),
    ]
