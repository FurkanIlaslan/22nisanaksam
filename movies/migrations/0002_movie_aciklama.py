# Generated by Django 4.2.3 on 2024-07-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='aciklama',
            field=models.TextField(blank=True, null=True),
        ),
    ]
