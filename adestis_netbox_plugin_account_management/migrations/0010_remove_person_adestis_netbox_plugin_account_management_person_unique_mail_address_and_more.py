# Generated by Django 4.1.10 on 2023-11-06 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adestis_netbox_plugin_account_management', '0009_remove_logincredentials_person'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='person',
            name='adestis_netbox_plugin_account_management_person_unique_mail_address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='person',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mail_address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='person_status',
        ),
        migrations.RemoveField(
            model_name='person',
            name='tenant',
        ),
    ]
