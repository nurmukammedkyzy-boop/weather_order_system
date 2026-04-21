import sqlite3

# Функция которая открывает соединение с базой
def get_connection(db_path: str = "weather.db") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row #С ней можно обращаться по названию столбца
    return conn

# создаёт таблицы в базе
def init_db(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor() #это инструмент, через который мы отправляем SQL-команды в базу.

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    conn.commit()


def create_user(conn: sqlite3.Connection, name: str, city: str) -> int:
    cursor = conn.cursor() # Создаём инструмент для SQL-команд
    cursor.execute(
        "INSERT INTO users (name, city) VALUES (?, ?)",
        (name, city)
    )
    conn.commit()
    return cursor.lastrowid


def get_user_by_id(conn: sqlite3.Connection, user_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


def create_order_record(conn: sqlite3.Connection, user_id: int, product: str) -> int:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (user_id, product) VALUES (?, ?)",
        (user_id, product)
    )
    conn.commit()
    return cursor.lastrowid


def get_order_by_id(conn: sqlite3.Connection, order_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    return cursor.fetchone()