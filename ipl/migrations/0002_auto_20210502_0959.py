# Generated by Django 3.2 on 2021-05-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipl', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iplmatch',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='iplmatch',
            name='date',
            field=models.DateField(),
        ),
    ]
