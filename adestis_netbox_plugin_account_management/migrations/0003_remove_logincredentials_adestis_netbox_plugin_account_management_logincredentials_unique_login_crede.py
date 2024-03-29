# Generated by Django 4.1.5 on 2023-03-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adestis_netbox_plugin_account_management', '0002_alter_system_system_url'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='logincredentials',
            name='adestis_netbox_plugin_account_management_logincredentials_unique_login_credentials',
        ),
        migrations.AddConstraint(
            model_name='logincredentials',
            constraint=models.UniqueConstraint(fields=('system', 'person', 'logon_name'), name='adestis_netbox_plugin_account_management_logincredentials_unique_login_credentials'),
        ),
    ]
