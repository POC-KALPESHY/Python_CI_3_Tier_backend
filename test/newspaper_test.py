import unittest
import requests
import json
import xmlrunner
import coverage

cov = coverage.coverage()
cov.start()

API_URL_HOME = "http://127.0.0.1:5002/home"
API_URL_SPORTS = "http://127.0.0.1:5002/sports"
API_URL_POLITICAL = "http://127.0.0.1:5002/political"


class ApiTest(unittest.TestCase):

    def test_1_get_home_success(self):
        response = requests.get(API_URL_HOME)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data)

    def test_2_get_sports_success(self):
        response = requests.get(API_URL_SPORTS)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data)

    def test_3_get_political_success(self):
        response = requests.get(API_URL_POLITICAL)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data)

    def test_4_get_home_invalid_route(self):
        invalid_url = "http://127.0.0.1:5002/invalid_home_route"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_5_get_sports_invalid_route(self):
        invalid_url = "http://127.0.0.1:5002/invalid_sports_route"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_6_get_political_invalid_route(self):
        invalid_url = "http://127.0.0.1:5002/invalid_political_route"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_7_get_home_empty_response(self):
        response = requests.get(API_URL_HOME)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data)  # Assuming an empty response is possible

    def test_8_get_sports_empty_response(self):
        response = requests.get(API_URL_SPORTS)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data)  # Assuming an empty response is possible

    def test_9_get_political_empty_response(self):
        response = requests.get(API_URL_POLITICAL)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data)  # Assuming an empty response is possible

    def test_10_get_home_invalid_method(self):
        response = requests.post(API_URL_HOME)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_11_get_sports_invalid_method(self):
        response = requests.post(API_URL_SPORTS)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_12_get_political_invalid_method(self):
        response = requests.post(API_URL_POLITICAL)
        self.assertEqual(response.status_code, 405)  # Method Not Allowed

    def test_13_get_home_valid_data(self):
        response = requests.get(API_URL_HOME)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNotNone(response_data)  # Assuming response data is not None

    def test_14_get_sports_valid_data(self):
        response = requests.get(API_URL_SPORTS)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNotNone(response_data)  # Assuming response data is not None

    def test_15_get_political_valid_data(self):
        response = requests.get(API_URL_POLITICAL)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsNotNone(response_data)  # Assuming response data is not None

    def test_16_get_home_invalid_parameters(self):
        invalid_url = "http://127.0.0.1:5002/home?invalid_param=value"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 400)  # Bad Request

    def test_17_get_sports_invalid_parameters(self):
        invalid_url = "http://127.0.0.1:5002/sports?invalid_param=value"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 400)  # Bad Request

    def test_18_get_political_invalid_parameters(self):
        invalid_url = "http://127.0.0.1:5002/political?invalid_param=value"
        response = requests.get(invalid_url)
        self.assertEqual(response.status_code, 400)  # Bad Request


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiTest)
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    result = runner.run(suite)

    cov.stop()
    cov.save()
    cov.xml_report(outfile='coverage.xml')
