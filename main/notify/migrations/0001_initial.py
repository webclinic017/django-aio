# Generated by Django 3.0.10 on 2021-03-08 19:17

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.notify.models.request


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('body', models.TextField(verbose_name='Description')),
                ('file', models.FileField(blank=True, null=True, upload_to=main.notify.models.request._handle_notification_file, verbose_name='File')),
                ('staff_only', models.BooleanField(default=False, verbose_name='User Staff Only')),
                ('requesttype', models.CharField(choices=[('general', 'General'), ('custom', 'Custom')], default='general', max_length=24, verbose_name='Request Type')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Received user Count')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Caller')),
                ('users', models.ManyToManyField(blank=True, related_name='notificationrequest_users', to=settings.AUTH_USER_MODEL, verbose_name='To Users')),
            ],
            options={
                'verbose_name': 'Notification Request',
                'verbose_name_plural': 'Notification Requests',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('read', models.BooleanField(default=False, verbose_name='Is read')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('body', models.TextField(verbose_name='Description')),
                ('href', models.TextField(blank=True, verbose_name='Extra Link')),
                ('fromuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fromuser_notification', to=settings.AUTH_USER_MODEL, verbose_name='From User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-created',),
            },
        ),
    ]
