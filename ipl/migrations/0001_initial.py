# Generated by Django 3.2 on 2021-05-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IplMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField(editable=False)),
                ('playerOfMatch', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('tossWinner', models.CharField(max_length=100)),
                ('tossDecision', models.CharField(max_length=100)),
                ('matchWinner', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('resultMargin', models.CharField(max_length=100)),
                ('umpire1', models.CharField(max_length=100)),
                ('umpire2', models.CharField(max_length=100)),
            ],
        ),
    ]
