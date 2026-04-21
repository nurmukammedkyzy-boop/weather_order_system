import requests # отправлять HTTP-запросы в API.

class WeatherAPIError(Exception):
    pass


# Функция проверки
def validate_weather_response(data: dict) -> dict:
    if not isinstance(data, dict):
        raise WeatherAPIError("Weather API returned non-dict response")

    if "temperature" not in data or "condition" not in data:
        raise WeatherAPIError("Weather API response missing required fields")

    if not isinstance(data["temperature"], (int, float)):
        raise WeatherAPIError("Invalid temperature type")

    if data["condition"] not in {"rain", "sunny", "snow"}:
        raise WeatherAPIError("Invalid weather condition")

    return {
        "temperature": float(data["temperature"]),
        "condition": data["condition"]
    }


# Главная функция для получения погоды
def get_weather(city: str, base_url: str = "https://example.com/weather", timeout: int = 5) -> dict:
    try:
        response = requests.get(base_url, params={"city": city}, timeout=timeout)
        response.raise_for_status() # Проверяет, был ли HTTP-статус успешным.
        data = response.json()
        return validate_weather_response(data) # Передаёт полученный ответ в функцию проверки
    except (requests.RequestException, ValueError, WeatherAPIError) as exc:
        raise WeatherAPIError(f"Failed to fetch weather for city '{city}': {exc}") from exc