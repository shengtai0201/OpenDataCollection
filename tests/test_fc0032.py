import unittest

from cwb.api.ElementName import TodayTomorrowThirtySixHours
from cwb.api.Enum import Format, Sort
from cwb.api.FC0032 import FC0032


class TestFC0032(unittest.TestCase):
    def test_payload_none(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        payload = api.test_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        api.set_limit(2)
        api.set_offset(1)
        api.set_format(Format.xml)
        api.add_location_name("宜蘭縣")
        api.add_location_name("花蓮縣")
        api.add_element_name(TodayTomorrowThirtySixHours.Wx)
        api.add_element_name(TodayTomorrowThirtySixHours.PoP)
        api.add_sort(Sort.time)

        payload = api.test_payload()
        print(payload)

    # def test_get_response_no_payload(self):
    #     api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
    #     response = api.get_response()
    #     data = response.json()
    #     print(data)

    # [1].一般天氣預報 - 今明36小時天氣預報
    def test_get_data_set_no_payload2(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        data_set = api.get_data_set()
        print(data_set)