from netbox.plugins import PluginConfig

class AdestisAccountManagementConfig(PluginConfig):
    name = 'adestis_netbox_plugin_account_management'
    verbose_name = 'Account Management'
    description = 'A NetBox plugin for managing the ownership of accounts.'
    version = '1.8.1'
    author = 'ADESTIS GmbH'
    author_email = 'pypi@adestis.de'
    base_url = 'account-management'
    required_settings = []
    default_settings = {}

config = AdestisAccountManagementConfig
