# Generated by Django 5.0.1 on 2024-01-14 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PreparationStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityNumber', models.FloatField()),
                ('quantityMeasure', models.CharField(choices=[('grams', 'Grams'), ('units', 'Units'), ('ounces', 'Ounces'), ('cups', 'Cups'), ('pieces', 'Pieces'), ('liters', 'Liters'), ('mililiters', 'Milliliters'), ('tablespoon', 'Tablespoon'), ('teaspoon', 'Teaspoon')], default='grams', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeName', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('chef', models.CharField(max_length=30)),
                ('ingredient', models.ManyToManyField(to='posts.ingredient')),
                ('preparationStep', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.preparationstep')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.ManyToManyField(null=True, to='posts.quantity'),
        ),
    ]
