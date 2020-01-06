
class SampleServiceError(Exception):
    """ sample service error """


class DownloadError(SampleServiceError):
    """ download error """


class SampleNotExist(SampleServiceError):
    """ sample not exist """
