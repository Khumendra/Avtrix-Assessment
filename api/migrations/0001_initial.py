# Generated by Django 4.1.3 on 2022-11-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]