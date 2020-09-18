# Generated by Django 2.2 on 2020-09-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricapp', '0007_auto_20200918_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='team',
        ),
        migrations.AddField(
            model_name='match',
            name='location',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='stadium',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.DeleteModel(
            name='PlayerDetail',
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]
