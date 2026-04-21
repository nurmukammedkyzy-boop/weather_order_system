# Weather-Based Order System

A small Python project that stores users in a database, fetches weather data from an external API, suggests a product based on weather conditions, and saves the order.

## Project Objective

This project was created for the assignment **"Testing a Service with Database & External API"**.

It demonstrates:

- unit testing
- integration testing
- working with a real database
- mocking an external API
- testing full flow scenarios

## Project Scenario

The system works like this:

1. A user is stored in the database with a name and city.
2. The system gets the weather for the user’s city.
3. Based on the weather condition, the system suggests a product.
4. The suggested product is saved as an order in the database.

## Functional Requirements

### Database Layer

The project uses **SQLite** as the database.

There are two tables:

#### `users`
- `id`
- `name`
- `city`

#### `orders`
- `id`
- `user_id`
- `product`
- `created_at`

### External API Integration

The project contains a function:

The main function:  create_order(user_id: int)

`python
get_weather(city: str) -> dict

`Project Structure
weather_order_system/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── service.py
│   └── weather_api.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_unit_service.py
│   ├── test_unit_weather_api.py
│   ├── test_unit_create_order.py
│   ├── test_integration_db.py
│   └── test_combined_real_db_mock_api.py
├── requirements.txt
└── pytest.ini
