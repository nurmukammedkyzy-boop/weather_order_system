import pytest

from app.service import suggest_product


@pytest.mark.parametrize( #Это способ проверить одну и ту же функцию на нескольких наборах данных
    "weather, expected",
    [
        ({"temperature": 10.0, "condition": "rain"}, "umbrella"),
        ({"temperature": 30.0, "condition": "sunny"}, "sunglasses"),
        ({"temperature": -5.0, "condition": "snow"}, "jacket"),
    ]
)
def test_suggest_product(weather, expected):
    assert suggest_product(weather) == expected


def test_suggest_product_invalid_condition():
    with pytest.raises(ValueError, match="Unsupported weather condition"):
        suggest_product({"temperature": 12.0, "condition": "storm"})