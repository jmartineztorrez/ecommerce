# Generated by Django 2.2.10 on 2020-03-04 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprint8', '0008_auto_20200304_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cesta',
            name='productos',
        ),
        migrations.AddField(
            model_name='cesta',
            name='productos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint8.Producto'),
        ),
    ]