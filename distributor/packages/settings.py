from django.conf import settings

STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages')
DEV_STORAGE_ROOT = getattr(settings, 'DEV_PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages_dev')

BRANCHES = {
    "master": STORAGE_ROOT,
    "develop": DEV_STORAGE_ROOT,
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
