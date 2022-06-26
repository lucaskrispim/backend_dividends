# Generated by Django 4.0.5 on 2022-06-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyanddividends',
            name='r1',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='r1'),
        ),
        migrations.AddField(
            model_name='companyanddividends',
            name='r3',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='r3'),
        ),
        migrations.AddField(
            model_name='companyanddividends',
            name='r5',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='r5'),
        ),
    ]