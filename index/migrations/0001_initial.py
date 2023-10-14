# Generated by Django 4.2.6 on 2023-10-14 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=512)),
                ('product_des', models.TextField(blank=True)),
                ('product_price', models.FloatField()),
                ('product_photo', models.ImageField(upload_to='index\\static\\img')),
                ('product_amount', models.IntegerField()),
                ('product_city', models.TextField(blank=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.category')),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_count', models.IntegerField()),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.product')),
            ],
        ),
    ]