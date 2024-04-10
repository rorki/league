# Generated by Django 4.1 on 2024-04-10 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_delete_coach_team_coach'),
        ('league', '0002_league_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.IntegerField(choices=[(16, '16th-finals'), (8, 'Eighth-finals'), (4, 'Quarterfinals'), (2, 'Semifinals'), (1, 'Final')], default=16)),
                ('team1_score', models.IntegerField(default=0)),
                ('team2_score', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='team.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='team.team')),
            ],
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
            ],
        ),
        migrations.DeleteModel(
            name='League',
        ),
    ]