from app.db import get_connection, init_db, create_user, get_order_by_id
from app.service import create_order


def test_combined_real_db_mock_api(mocker):
    conn = get_connection(":memory:")
    init_db(conn)

    user_id = create_user(conn, "Dana", "Astana")

    mocker.patch(
        "app.service.get_weather",
        return_value={"temperature": -12.0, "condition": "snow"}
    )

    order = create_order(conn, user_id)

    assert order is not None
    assert order["user_id"] == user_id
    assert order["product"] == "jacket"