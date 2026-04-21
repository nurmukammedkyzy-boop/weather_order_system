from app.db import (
    get_connection,
    init_db,
    create_user,
    get_user_by_id,
    create_order_record,
    get_order_by_id,
)


def test_integration_create_user_and_order():
    conn = get_connection(":memory:") # Создаём временную SQLite-базу в памяти, а не в файле
    init_db(conn)

    user_id = create_user(conn, "Aruzhan", "Almaty")
    user = get_user_by_id(conn, user_id)

    assert user is not None
    assert user["name"] == "Aruzhan"
    assert user["city"] == "Almaty"

    order_id = create_order_record(conn, user_id, "umbrella")
    order = get_order_by_id(conn, order_id)

    assert order is not None
    assert order["user_id"] == user_id
    assert order["product"] == "umbrella"