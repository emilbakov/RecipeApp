# Generated by Django 2.1.15 on 2020-02-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200210_1748'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='RecipeCategory',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='tags',
            new_name='recipeCategory',
        ),
    ]
