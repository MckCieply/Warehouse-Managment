# Generated by Django 4.1.5 on 2023-02-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('FOO', 'Food'), ('BE', 'Beauty'), ('CLO', 'Clothes'), ('HE', 'Health'), ('ACC', 'Accessories')], max_length=3)),
            ],
        ),
    ]
