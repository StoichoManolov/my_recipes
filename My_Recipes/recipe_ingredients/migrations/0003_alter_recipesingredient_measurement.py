# Generated by Django 5.1.3 on 2024-11-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_ingredients', '0002_recipesingredient_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesingredient',
            name='measurement',
            field=models.CharField(choices=[('Tablespoon', 'Tablespoon'), ('Teaspoon', 'Teaspoon'), ('Cup', 'Cup'), ('Milliliter', 'Milliliter'), ('Liter', 'Liter'), ('Drop', 'Drop'), ('GRAM', 'GRAM'), ('Kilogram', 'Kilogram'), ('Milligram', 'Milligram')], max_length=50),
        ),
    ]
