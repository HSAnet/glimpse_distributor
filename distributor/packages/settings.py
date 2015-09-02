from django.conf import settings

STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages')
DEV_STORAGE_ROOT = getattr(settings, 'DEV_PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages_dev')
MPLANE_STORAGE_ROOT = getattr(settings, 'MPLANE_PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages_mplane')

DEBUG_SYMBOL_STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '/var/www/distributor/debug_symbols')
DEBUG_SYMBOL_DEV_STORAGE_ROOT = getattr(settings, 'DEV_PACKAGES_STORAGE_ROOT', '/var/www/distributor/debug_symbols_dev')
DEBUG_SYMBOL_MPLANE_STORAGE_ROOT = getattr(settings, 'MPLANE_PACKAGES_STORAGE_ROOT', '/var/www/distributor/debug_symbols_mplane')

PACKAGE_BRANCHES = {
    "master": STORAGE_ROOT,
    "develop": DEV_STORAGE_ROOT,
    "mplane_interface": MPLANE_STORAGE_ROOT,
}

DEBUG_SYMBOL_BRANCHES = {
    "master": DEBUG_SYMBOL_STORAGE_ROOT,
    "develop": DEBUG_SYMBOL_DEV_STORAGE_ROOT,
    "mplane_interface": DEBUG_SYMBOL_MPLANE_STORAGE_ROOT,
}

CHANNEL_SETTINGS = getattr(settings, 'PACKAGE_CHANNEL_SETTINGS', {
    'ubuntu-trusty': 'UbuntuTrustyHandler',
    'ubuntu-precise': 'UbuntuPreciseHandler',
    'rpi-raspbian': 'RpiRaspbianHandler',
    'rpi-raspbian-jessie': 'RpiRaspbianJessieHandler',
    'debian-jessie': 'DebianJessieHandler',
    'ubuntu-trusty-armhf': 'UbuntuTrustyArmhfHandler',
    'ubuntu-utopic': 'UbuntuUtopicHandler',
    'windows': 'WindowsHandler'
})
