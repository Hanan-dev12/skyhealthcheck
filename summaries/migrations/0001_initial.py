# Generated by Django 5.1.7 on 2025-03-30 06:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health_cards', '0002_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('green_count', models.IntegerField(default=0)),
                ('amber_count', models.IntegerField(default=0)),
                ('red_count', models.IntegerField(default=0)),
                ('improving_count', models.IntegerField(default=0)),
                ('stable_count', models.IntegerField(default=0)),
                ('declining_count', models.IntegerField(default=0)),
                ('comments_summary', models.TextField(blank=True, help_text='AI-generated summary of all comments', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_cards.healthcard')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_cards.healthchecksession')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='teams.team')),
            ],
            options={
                'verbose_name_plural': 'Team summaries',
                'unique_together': {('team', 'card', 'session')},
            },
        ),
        migrations.CreateModel(
            name='VoteSummary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quarter', models.CharField(max_length=2)),
                ('year', models.IntegerField()),
                ('green_percentage', models.FloatField(default=0)),
                ('amber_percentage', models.FloatField(default=0)),
                ('red_percentage', models.FloatField(default=0)),
                ('trend', models.CharField(default='stable', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_cards.healthcard')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_history', to='teams.team')),
            ],
            options={
                'ordering': ['-year', '-quarter'],
                'unique_together': {('team', 'card', 'quarter', 'year')},
            },
        ),
    ]
