# Generated by Django 3.2.8 on 2021-12-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfitShowroomApp', '0007_auto_20211210_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='ocasiones',
            field=models.ManyToManyField(to='outfitShowroomApp.Ocasion'),
        ),
        migrations.AlterField(
            model_name='outfit',
            name='prendas',
            field=models.ManyToManyField(to='outfitShowroomApp.Prenda'),
        ),
    ]
