# Generated by Django 5.0.4 on 2024-05-15 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlshield', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlshield.datasource')),
            ],
        ),
        migrations.CreateModel(
            name='TableColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_type', models.CharField(blank=True, max_length=50)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlshield.table')),
            ],
        ),
        migrations.CreateModel(
            name='TableSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlshield.datasource')),
                ('tables', models.ManyToManyField(blank=True, to='sqlshield.table')),
            ],
        ),
    ]
