# Generated by Django 5.0.4 on 2024-07-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terno', '0023_queryhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='queryhistory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
