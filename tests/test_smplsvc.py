# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock, call

from smplsvc.infra import SampleService
from smplsvc.exceptions import DownloadError, SampleNotExist


class SampleServiceTestCase(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_smplsvc(self):
        smplsvc = SampleService()
        assert smplsvc

    def test_smpl_download(self):
        smplsvc = SampleService()
        hash = None
        with self.assertRaises(DownloadError) as context:
            smplsvc.download(hash)
        hash = ""
        with self.assertRaises(SampleNotExist) as context:
            smplsvc.download(hash)
        hash = "some_hash"
        res = smplsvc.download(hash)
        assert res
