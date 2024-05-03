import requests

API_URL_HOME = "http://127.0.0.1:5002/home"
API_URL_SPORTS = "http://127.0.0.1:5002/sports"
API_URL_POLITICAL = "http://127.0.0.1:5002/political"


def test_get_home_success():
    response = requests.get(API_URL_HOME)
    assert response.status_code == 200
    assert response.json()


def test_get_sports_success():
    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 200
    assert response.json()


def test_get_political_success():
    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 200
    assert response.json()


def test_get_home_invalid_route():
    invalid_url = "http://127.0.0.1:5002/invalid_home_route"
    response = requests.get(invalid_url)
    assert response.status_code == 404


def test_get_sports_invalid_route():
    invalid_url = "http://127.0.0.1:5002/invalid_sports_route"
    response = requests.get(invalid_url)
    assert response.status_code == 404


def test_get_political_invalid_route():
    invalid_url = "http://127.0.0.1:5002/invalid_political_route"
    response = requests.get(invalid_url)
    assert response.status_code == 404


def test_get_home_empty_response():
    response = requests.get(API_URL_HOME)
    assert response.status_code == 200
    assert not response.json()


def test_get_sports_empty_response():
    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 200
    assert not response.json()


def test_get_political_empty_response():
    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 200
    assert not response.json()


def test_get_home_invalid_method():
    response = requests.post(API_URL_HOME)
    assert response.status_code == 405


def test_get_sports_invalid_method():
    response = requests.post(API_URL_SPORTS)
    assert response.status_code == 405


def test_get_political_invalid_method():
    response = requests.post(API_URL_POLITICAL)
    assert response.status_code == 405


def test_get_home_valid_data():
    response = requests.get(API_URL_HOME)
    assert response.status_code == 200
    assert response.json() is not None


def test_get_sports_valid_data():
    response = requests.get(API_URL_SPORTS)
    assert response.status_code == 200
    assert response.json() is not None


def test_get_political_valid_data():
    response = requests.get(API_URL_POLITICAL)
    assert response.status_code == 200
    assert response.json() is not None
