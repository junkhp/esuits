# Generated by Django 3.1.1 on 2020-11-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esuits', '0019_auto_20201130_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyhomepageurlmodel',
            name='word_cloud_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ワードクラウドパス'),
        ),
    ]
