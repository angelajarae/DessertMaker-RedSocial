# Generated by Django 5.0.1 on 2024-01-17 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_ingredient_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.CreateModel(
            name='Ingredient_Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.ingredient')),
                ('quantity', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.quantity')),
                ('recipe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
