"""Test fixtures."""

import pytest
from lxml import etree

from napalm.base.test import conftest as parent_conftest

from napalm.base.test.double import BaseTestDouble

from napalm_sros import sros


@pytest.fixture(scope="class")
def set_device_parameters(request):
    """Set up the class."""

    def fin():
        request.cls.device.close()

    request.addfinalizer(fin)

    request.cls.driver = sros.NokiaSROSDriver
    request.cls.patched_driver = PatchedNokiaSROSDriver
    request.cls.vendor = "sros"
    parent_conftest.set_device_parameters(request)


def pytest_generate_tests(metafunc):
    """Generate test cases dynamically."""
    parent_conftest.pytest_generate_tests(metafunc, __file__)


class PatchedNokiaSROSDriver(sros.NokiaSROSDriver):
    """Patched NokiaSROS Driver."""

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        # optional_args["config_lock"] = False  # to not try lock on open() # Juniper mentioned it
        super(self.__class__, self).__init__(
            hostname, username, password, timeout, optional_args
        )

        self.patched_attrs = ["device"]
        self.device = FakeNokiaSROSDevice()


class FakeNokiaSROSDevice(BaseTestDouble):
    def __init__(self):
        self.get = FakeGetMethod(self)

    def open(self):
        pass

    def close(self):
        pass


class FakeGetMethod:
    """
    Fake Get Method.
    """

    def __init__(self, device):
        self._device = device

    def response(self, filter="", with_defaults=""):

        filename = "sros/mock_data/filename.txt"
        filepath = self._device.find_file(filename)
        response_string = self._device.read_txt_file(filepath)

        return FakeGetReply(data=response_string)

    __call__ = response


class FakeGetReply:
    """
    Will fake the GetReply class of ncclient
    """

    def __init__(self, data):
        self._data = data

    @property
    def data_xml(self):
        return to_ele(etree.fromstring(self._data.encode("UTF-8")))


def to_ele(x):
    return x if etree.iselement(x) else etree.fromstring(x.encode("UTF-8"))
