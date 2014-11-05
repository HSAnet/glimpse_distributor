from django.conf import settings

STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '/var/www/distributor/packages')

CHANNEL_SETTINGS = getattr(settings, 'PACKAGE_CHANNEL_SETTINGS', {
    'ubuntu-trusty': 'UbuntuTrustyHandler',
    'ubuntu-precise': 'UbuntuPreciseHandler',
    'rpi-raspbian': 'RpiRaspbianHandler',
    'rpi-raspbian-jessie': 'RpiRaspbianJessieHandler',
    'debian-jessie': 'DebianJessieHandler'
})
