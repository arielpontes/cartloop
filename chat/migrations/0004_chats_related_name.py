# Generated by Django 3.1.3 on 2020-11-07 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_refactor_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chat.conversation'),
        ),
    ]