# Generated by Django 5.1.3 on 2024-11-29 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userimports_content2'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIntegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(blank=True, max_length=500, null=True)),
                ('token', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_integration', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]