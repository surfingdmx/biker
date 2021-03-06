# Generated by Django 2.2.4 on 2019-08-29 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Route'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='destination_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='note',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
