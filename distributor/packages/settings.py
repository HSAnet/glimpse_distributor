from django.conf import settings


STORAGE_ROOT = getattr(settings, 'PACKAGES_STORAGE_ROOT', '')

CHANNEL_SETTINGS = getattr(settings, 'PACKAGE_CHANNEL_SETTINGS', {
    'debian-amd64': 'DebianAMD64Handler',
    'fedora-amd64': 'FedoraAMD64Handler',
    'arch-amd64': 'ArchAMD64Handler',
})

