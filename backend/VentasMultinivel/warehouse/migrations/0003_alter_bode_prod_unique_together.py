# Generated by Django 4.0.3 on 2023-03-16 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_alter_bode_prod_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bode_prod',
            unique_together=set(),
        ),
    ]