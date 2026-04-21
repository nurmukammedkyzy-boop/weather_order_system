import pytest

from app.service import create_order, OrderCreationError


def test_create_order_success(mocker):
    fake_conn = mocker.Mock() # фейковое подключение к базе

    fake_user = {"id": 1, "name": "Dana", "city": "Almaty"}
    fake_order = {"id": 10, "user_id": 1, "product": "umbrella"}

    mocker.patch("app.service.get_user_by_id", return_value=fake_user)
    mocker.patch("app.service.get_weather", return_value={"temperature": 9.0, "condition": "rain"})
    mocker.patch("app.service.create_order_record", return_value=10)
    mocker.patch("app.service.get_order_by_id", return_value=fake_order)

    result = create_order(fake_conn, 1)

    assert result["product"] == "umbrella"


def test_create_order_user_not_found(mocker):
    fake_conn = mocker.Mock()
    mocker.patch("app.service.get_user_by_id", return_value=None)

    with pytest.raises(OrderCreationError, match="User with id=999 not found"):
        create_order(fake_conn, 999)


def test_create_order_db_failure(mocker):
    fake_conn = mocker.Mock()
    fake_user = {"id": 1, "name": "Dana", "city": "Almaty"}

    mocker.patch("app.service.get_user_by_id", return_value=fake_user)
    mocker.patch("app.service.get_weather", return_value={"temperature": 25.0, "condition": "sunny"})
    mocker.patch("app.service.create_order_record", side_effect=Exception("DB insert failed")) # при попытке сохранить заказ выбросить ошибку базы

    with pytest.raises(OrderCreationError, match="Database failure: DB insert failed"):
        create_order(fake_conn, 1)