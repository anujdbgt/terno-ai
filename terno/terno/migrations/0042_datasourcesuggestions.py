# Generated by Django 5.1.1 on 2025-03-20 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terno', '0041_organisation_assign_llm_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasourceSuggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.TextField(blank=True, null=True)),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.datasource')),
            ],
        ),
    ]
