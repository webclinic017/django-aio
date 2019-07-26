# Generated by Django 2.2.3 on 2019-07-26 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Caller'),
        ),
        migrations.AddField(
            model_name='notificationrequest',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='notificationrequest_users', to=settings.AUTH_USER_MODEL, verbose_name='To Users'),
        ),
        migrations.AddField(
            model_name='notification',
            name='fromuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fromuser_notification', to=settings.AUTH_USER_MODEL, verbose_name='From User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]