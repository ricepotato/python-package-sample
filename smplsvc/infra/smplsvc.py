from ..exceptions.exc import DownloadError, SampleNotExist
from .mod import InfraMod


class SampleService(object):
    def __init__(self):
        self.mod = InfraMod()

    def download(self, hash):
        if hash is None:
            raise DownloadError("download error")
        if self.mod.exist(hash):
            return "/path/to/file"
        else:
            raise SampleNotExist("sample not exist")
