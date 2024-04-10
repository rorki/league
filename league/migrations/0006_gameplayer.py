# Generated by Django 4.1 on 2024-04-10 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_delete_coach_team_coach'),
        ('league', '0005_delete_gameplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]