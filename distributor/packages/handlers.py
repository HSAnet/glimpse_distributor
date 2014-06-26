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

        print(package_file.read())

        with open(self.file_path, 'wb') as f:
            f.write(package_file.read())


class DebianAMD64Handler(PackageUploadHandler):
    file_path = './debian'


class FedoraAMD64Handler(PackageUploadHandler):
    file_path = './fedora'
    

class ArchAMD64Handler(PackageUploadHandler):
    file_path = './arch'
