# Generated by Django 2.2.11 on 2020-04-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200225_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_x',
            field=models.URLField(blank=True),
        ),
    ]