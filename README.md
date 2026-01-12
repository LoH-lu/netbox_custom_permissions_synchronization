# netbox-custom-permissions-synchronization

## Overview

This plugin allows you to compare and synchronize objects custom permissions (tenant assignments and custom permission fields) from their parent objects in NetBox. It's useful for ensuring consistent permission and tenant assignments across all objects within a parent object.

## Features

- Compare objects custom permissions against their parent object
- View tenant and permission field assignments at a glance
- Synchronize all objects with parent object permissions
- Automatic detection of mismatched permissions
- User-friendly interface with color-coded status indicators

## Compatibility

Tested with NetBox versions 4.3.7-4.4.10.

## Installation

If your NetBox installation uses virtualenv, activate it like this:

```bash
source /opt/netbox/venv/bin/activate
```

Install the plugin from PyPI:

```bash
pip install netbox-custom-permissions-synchronization
```

Or clone this repository, then go to the folder with it and install the plugin:

```bash
pip install .
```

To enable the plugin, add the plugin's name to the `PLUGINS` list in `configuration.py` (it's usually located in `/opt/netbox/netbox/netbox/`) like so:

```python
PLUGINS = [
    'netbox_custom_permissions_synchronization'
]
```

Don't forget to restart NetBox:

```bash
sudo systemctl restart netbox netbox-rq
```

## Usage

Navigate to any parent object in NetBox and look for the "Sync Permissions" button at the top of the page:

The synchronization page will show:
- Parent object information including tenant and permission assignments
- Objects that need synchronization (highlighted in yellow)
- Objects that are already synchronized (highlighted in green)

Select the objects you want to synchronize using the checkboxes, then click:
- **"Sync All IPs"** - Synchronize all IP addresses in the prefix
- **"Sync All Interfaces"** - Synchronize all Interfaces in Virtual Machines
- **"Sync All Virtual Disks"** - Synchronize all Virtual Disks in Virtual Machines

## Custom Fields Required

This plugin requires the following custom fields to be created in NetBox:

1. **tenant_permissions** - Multiple objects (Tenant) field to store read-write permission assignments
2. **tenant_permissions_ro** - Multiple objects (Tenant) field to store read-only permission assignments

These fields should be applied to both:
- IPAM > Prefix
- IPAM > IP Address
- Virtualization > Virtual Machine
- Virtualization > Interface
- Virtualization > Virtual Disk

## How It Works (example with IP addresses and Prefix)

1. When you access the sync page for a prefix, the plugin fetches all IP addresses within that prefix
2. It compares each IP address's tenant and permission fields with the parent prefix
3. IP addresses with mismatched values are marked for synchronization
4. You can selectively sync individual IPs or all IPs at once
5. The sync operation updates:
   - Tenant assignment (if the prefix has a tenant set)
   - `tenant_permissions` custom field
   - `tenant_permissions_ro` custom field

## Plugin Settings

If you want to override the default values, configure the `PLUGINS_CONFIG` in your `configuration.py`:

```python
PLUGINS_CONFIG = {
    'netbox_custom_permissions_synchronization': {
        # Add any future configuration options here
    }
}
```

Currently, there are no required configuration options. All settings are managed through the NetBox UI.

## Troubleshooting

### Custom fields not syncing
- Ensure that the `tenant_permissions` and `tenant_permissions_ro` custom fields exist in NetBox
- Verify that these custom fields are assigned to Prefix, IP Address and Virtualization models
- Check that the field names match exactly (case-sensitive)

### No IP addresses found
- Make sure the prefix status is not "container" (container prefixes are skipped)
- Verify that IP addresses exist within the prefix range
- Check that you have permission to view the IP addresses

### Permission denied errors
- Ensure your user account has the required permissions listed above
- Contact your NetBox administrator if you lack necessary permissions

## Support

For issues, feature requests, or contributions, please visit the [project repository](https://github.com/LoH-lu/netbox_ip_permissions_synchronization/).

## License

GNU General Public License v3.0 - See LICENSE file for details.

## Acknowledgements

This project was inspired in part by the work done in the `netbox-interface-synchronization` plugin by NetTech2001.
Their approach to interface synchronization in NetBox provided valuable guidance when designing the permission-sync logic for IP addresses.
A big thanks to them for sharing their project with the community!
