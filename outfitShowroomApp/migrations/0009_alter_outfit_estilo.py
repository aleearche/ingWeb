# Generated by Django 3.2.8 on 2021-12-10 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outfitShowroomApp', '0008_auto_20211210_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfit',
            name='estilo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfitShowroomApp.estilo'),
        ),
    ]
