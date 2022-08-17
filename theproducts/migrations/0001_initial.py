# Generated by Django 3.2.13 on 2022-08-17 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('offer', models.IntegerField(null=True)),
                ('offerstatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('offerproduct', models.IntegerField(null=True)),
                ('image', models.CharField(max_length=2500)),
                ('image1', models.CharField(max_length=2500, null=True)),
                ('image2', models.CharField(max_length=2500, null=True)),
                ('offerstatuspro', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='theproducts.categoryies')),
            ],
        ),
    ]
