# Generated by Django 3.0.2 on 2020-05-08 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('user', '0002_auto_20200507_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='actionset',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='auth.Permission'),
        ),
    ]
