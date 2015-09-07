import os
import errno
import subprocess
import tarfile

from distributor.packages.settings import PACKAGE_BRANCHES,DEBUG_SYMBOLS_STORAGE_ROOT


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


class DebugSymbolsUploadHandler(object):
    file_path = DEBUG_SYMBOLS_STORAGE_ROOT

    @classmethod
    def handle_upload(self, debug_symbols_file):
        # store debug symbols to filesystem
        mkdir_p(self.file_path)
        tar = tarfile.open(mode="r:gz", fileobj=debug_symbols_file)
        tar.extractall(self.file_path)


class PackageUploadHandler(object):
    file_path = None

    @classmethod
    def handle_upload(self, package_name, package_file, branch):
        print(package_name, package_file)
        print(type(package_name), type(package_file))
        self.store_upload(package_file, branch)

    @classmethod
    def store_upload(self, package_file, branch):
        if self.file_path is None:
            raise Exception("Please define a file name for uploaded packages of this channel.")

        if branch not in PACKAGE_BRANCHES:
            raise Exception("Branch not allowed")

        # store package to filesystem
        absolute_dir = PACKAGE_BRANCHES[branch] + '/' + self.file_path
        mkdir_p(absolute_dir)
        absolute_file_path = absolute_dir + '/' + package_file.name
        with open(absolute_file_path, 'wb') as f:
            f.write(package_file.read())

        self.update_package_index(PACKAGE_BRANCHES[branch])

    @classmethod
    def update_package_index(self, cwd):
        pass


class UbuntuTrustyHandler(PackageUploadHandler):
    file_path = 'ubuntu-trusty'

    @classmethod
    def update_package_index(self, cwd):
        command = "dpkg-scanpackages %s /dev/null | gzip > %s/Packages.gz" % (self.file_path, self.file_path)
        subprocess.call(command, cwd=cwd, shell=True)


class UbuntuPreciseHandler(UbuntuTrustyHandler):
    file_path = 'ubuntu-percise'


class UbuntuTrustyArmhfHandler(UbuntuTrustyHandler):
    file_path = 'ubuntu-trusty-armhf'


class UbuntuUtopicHandler(UbuntuTrustyHandler):
    file_path = 'ubuntu-utopic'


class UbuntuVividHandler(UbuntuTrustyHandler):
    file_path = 'ubuntu-vivid'


class RpiRaspbianHandler(UbuntuTrustyHandler):
    file_path = 'rpi-raspbian'


class RpiRaspbianJessieHandler(UbuntuTrustyHandler):
    file_path = 'rpi-raspbian-jessie'


class DebianJessieHandler(UbuntuTrustyHandler):
    file_path = 'debian-jessie'


class WindowsHandler(PackageUploadHandler):
    file_path = 'windows'
