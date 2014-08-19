import os
import errno
import subprocess

from distributor.packages.settings import STORAGE_ROOT


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


class PackageUploadHandler(object):
    file_path = None

    @classmethod
    def handle_upload(self, package_name, package_file):
        print(package_name, package_file)
        print(type(package_name), type(package_file))
        self.store_upload(package_file)

    @classmethod
    def store_upload(self, package_file):
        if self.file_path is None:
            raise Exception("Please define a file name for uploaded packages of this channel.")

        absolute_dir = STORAGE_ROOT + '/' + self.file_path
        mkdir_p(absolute_dir)

        absolute_file_path = absolute_dir + '/' + package_file.name

        with open(absolute_file_path, 'wb') as f:
            f.write(package_file.read())

        self.update_package_index()

    @classmethod
    def update_package_index(self):
        pass


class UbuntuTrustyHandler(PackageUploadHandler):
    file_path = 'ubuntu-trusty'

    @classmethod
    def update_package_index(self):
        command = "dpkg-scanpackages %s /dev/null | gzip > %s/Packages.gz" % (self.file_path, self.file_path)
        subprocess.call(command, cwd=STORAGE_ROOT, shell=True)


class UbuntuPreciseHandler(UbuntuTrustyHandler):
    file_path = 'ubuntu-trusty'


class RpiRaspbianHandler(UbuntuTrustyHandler):
    file_path = 'rpi-raspbian'

