from app.db import get_user_by_id, create_order_record, get_order_by_id
from app.weather_api import get_weather, WeatherAPIError


class UserNotFoundError(Exception):
    pass


class OrderCreationError(Exception):
    pass

# Функция получает погоду и возвращает товар
def suggest_product(weather: dict) -> str:
    condition = weather.get("condition")

    mapping = {
        "rain": "umbrella",
        "sunny": "sunglasses",
        "snow": "jacket"
    }

    if condition not in mapping:
        raise ValueError(f"Unsupported weather condition: {condition}")

    return mapping[condition]


def create_order(conn, user_id: int):
    try:
        user = get_user_by_id(conn, user_id)
        if not user:
            raise UserNotFoundError(f"User with id={user_id} not found")

        weather = get_weather(user["city"])
        product = suggest_product(weather)
        order_id = create_order_record(conn, user_id, product) # Сохраняет заказ в базу
        return get_order_by_id(conn, order_id)

    except (UserNotFoundError, WeatherAPIError, ValueError) as exc:
        raise OrderCreationError(str(exc)) from exc
    except Exception as exc:
        raise OrderCreationError(f"Database failure: {exc}") from exc