# Generated by Django 2.2.4 on 2019-08-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img_url', models.URLField()),
                ('c_id', models.CharField(max_length=50)),
                ('c_type', models.CharField(max_length=50)),
                ('faction', models.CharField(max_length=50)),
                ('rarity', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=50)),
                ('attack', models.PositiveIntegerField()),
                ('health', models.PositiveIntegerField(default=10)),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cards', models.ManyToManyField(to='cards.Card')),
            ],
        ),
    ]
