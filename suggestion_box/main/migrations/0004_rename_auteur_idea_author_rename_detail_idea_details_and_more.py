# Generated by Django 4.1.7 on 2023-03-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_idea_auteur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='auteur',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='detail',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='formulation',
            new_name='name',
        ),
        migrations.AddField(
            model_name='idea',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
