# Generated by Django 5.1.1 on 2024-11-08 09:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('terno', '0035_alter_llmconfiguration_llm_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=100, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationDataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('datasource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.datasource')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationLLM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('llm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.llmconfiguration')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terno.organisation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
