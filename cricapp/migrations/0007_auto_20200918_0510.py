# Generated by Django 2.2 on 2020-09-17 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricapp', '0006_auto_20200917_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='match_location',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_stadium',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_tournament',
        ),
        migrations.RemoveField(
            model_name='match',
            name='teams',
        ),
        migrations.RemoveField(
            model_name='team',
            name='point',
        ),
        migrations.AddField(
            model_name='match',
            name='level',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='cricapp.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='cricapp.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team_winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_winner', to='cricapp.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(default='s', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cricapp.Team')),
            ],
            options={
                'verbose_name_plural': 'Points',
            },
        ),
    ]
