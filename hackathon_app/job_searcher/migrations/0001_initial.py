# Generated by Django 3.0.3 on 2020-02-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('summary', models.TextField()),
                ('location', models.TextField()),
                ('company', models.TextField()),
                ('url', models.URLField()),
                ('listing_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('city', models.TextField()),
                ('state', models.CharField(max_length=2)),
            ],
        ),
    ]
