import unittest, requests, ipaddress
from src.api_client import get_location
from unittest.mock import patch


class ApiClientTests(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "Florida",
            "cityName": "Miami",
            "language": "English",
            "currency": {"code": "USD"},
            "zipCode": "33101",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "Miami")
        self.assertEqual(result.get("language"), "English")
        self.assertEqual(result.get("currency"), "USD")
        self.assertEqual(result.get("zip_code"), "33101")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "Florida",
                    "cityName": "Miami",
                    "language": "English",
                    "currency": {"code": "USD"},
                    "zipCode": "33101",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "Miami")
        self.assertEqual(result.get("language"), "English")
        self.assertEqual(result.get("currency"), "USD")
        self.assertEqual(result.get("zip_code"), "33101")

    @patch("src.api_client.requests.get")
    def test_get_location_with_invalid_ip_throw_exception(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException(
                "does not appear to be an IPv4 or IPv6 address"
            ),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "Florida",
                    "cityName": "Miami",
                    "language": "English",
                    "currency": {"code": "USD"},
                    "zipCode": "33101",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "Florida")
        self.assertEqual(result.get("city"), "Miami")
        self.assertEqual(result.get("language"), "English")
        self.assertEqual(result.get("currency"), "USD")
        self.assertEqual(result.get("zip_code"), "33101")
