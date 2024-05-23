#!/bin/bash
rm -rf dist/ &&
rm -rf adestis_netbox_plugin_account_management.egg-info/ &&
rm -rf build/
py setup.py sdist bdist_wheel && 
py -m twine upload dist/* &&
rm -rf dist/ &&
rm -rf adestis_netbox_plugin_account_management.egg-info/ &&
rm -rf build/