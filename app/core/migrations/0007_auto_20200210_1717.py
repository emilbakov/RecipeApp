# Generated by Django 2.1.15 on 2020-02-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200210_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='price',
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipeYield',
            field=models.IntegerField(null=True),
        ),
    ]
