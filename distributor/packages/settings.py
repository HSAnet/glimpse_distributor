from django.conf import settings
from os.path import expanduser

STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '%s/packages' % (expanduser('~')))

CHANNEL_SETTINGS = getattr(settings, 'PACKAGE_CHANNEL_SETTINGS', {
    'ubuntu-trusty': 'UbuntuTrustyHandler',
    'ubuntu-precise': 'UbuntuPreciseHandler',
    'rpi-raspbian': 'RpiRaspbianHandler'
})
