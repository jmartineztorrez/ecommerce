# Generated by Django 2.2.10 on 2020-03-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint8', '0003_auto_20200228_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/img/'),
        ),
    ]
