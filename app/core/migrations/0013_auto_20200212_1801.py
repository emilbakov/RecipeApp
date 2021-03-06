# Generated by Django 2.1.15 on 2020-02-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200212_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='core.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipeCategory',
            field=models.ManyToManyField(blank=True, to='core.RecipeCategory'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipeYield',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
