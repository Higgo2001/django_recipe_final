# Generated by Django 5.0.6 on 2024-06-30 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flask_app', '0012_recipeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='Description',
        ),
    ]