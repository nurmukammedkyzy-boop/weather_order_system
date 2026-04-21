import pytest
import requests

from app.weather_api import get_weather, WeatherAPIError


def test_get_weather_success(mocker):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None # ошибок HTTP нет
    mock_response.json.return_value = { # если вызвать .json, вернётся вот такой словарь
        "temperature": 22.5,
        "condition": "sunny"
    }

    mocker.patch("app.weather_api.requests.get", return_value=mock_response) #Подменяет настоящий requests.get() на фейковый.

    result = get_weather("Almaty")
    assert result == {"temperature": 22.5, "condition": "sunny"}


def test_get_weather_invalid_response(mocker):
    mock_response = mocker.Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "temperature": 22.5 # нет condition
    }

    mocker.patch("app.weather_api.requests.get", return_value=mock_response)

    with pytest.raises(WeatherAPIError, match="missing required fields"):
        get_weather("Almaty")


def test_get_weather_timeout(mocker):
    mocker.patch(
        "app.weather_api.requests.get",
        side_effect=requests.Timeout("Request timed out")
    )

    with pytest.raises(WeatherAPIError, match="Request timed out"):
        get_weather("Almaty")