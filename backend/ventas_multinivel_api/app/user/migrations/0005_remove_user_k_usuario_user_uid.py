# Generated by Django 4.1.7 on 2023-03-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_k_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='k_usuario',
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
