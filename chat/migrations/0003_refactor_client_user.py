# Generated by Django 3.1.3 on 2020-11-07 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_chat_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='client',
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='client_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]