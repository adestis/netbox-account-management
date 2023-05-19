# Generated by Django 4.1.5 on 2023-03-13 17:28

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0084_staging'),
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=130)),
                ('system_url', models.URLField(max_length=2048)),
                ('system_status', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('first_name', models.CharField(max_length=130)),
                ('last_name', models.CharField(max_length=130)),
                ('mail_address', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True)),
                ('person_status', models.CharField(max_length=50)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Users',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='LoginCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('logon_name', models.CharField(max_length=254)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_to', models.DateField(blank=True, null=True)),
                ('login_credentials_status', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adestis_netbox_plugin_account_management.person')),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adestis_netbox_plugin_account_management.system')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Login Credentials',
                'verbose_name_plural': 'Login Credentials',
                'ordering': ('person',),
            },
        ),
        migrations.AddConstraint(
            model_name='system',
            constraint=models.UniqueConstraint(fields=('system_url',), name='adestis_netbox_plugin_account_management_system_unique_system_url'),
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('mail_address',), name='adestis_netbox_plugin_account_management_person_unique_mail_address'),
        ),
        migrations.AddConstraint(
            model_name='logincredentials',
            constraint=models.UniqueConstraint(fields=('system', 'person'), name='adestis_netbox_plugin_account_management_logincredentials_unique_login_credentials'),
        ),
    ]
