# Generated by Django 3.1.1 on 2020-12-17 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esuits', '0020_auto_20201130_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, to='esuits.TagModel', verbose_name='タグ名'),
        ),
    ]