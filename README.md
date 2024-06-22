# Online Store Inventory and Supplier Management API

## Overview

This project provides an API for managing inventory items and suppliers in an online store. It allows for the creation, retrieval, updating, and deletion of inventory items and suppliers, as well as the establishment of relationships between them. The API is designed to be utilized by various internal systems, including the front-end interface and the inventory tracking system.

## Features

- **Inventory Item Management**: Add, view, update, and remove items from the inventory.
- **Supplier Management**: Add new suppliers, update their details, and view their information.
- **Relationship Management**: Manage relationships between inventory items and suppliers.
- **Data Accessibility**: Ensure data is accessible in a format compatible with other systems (like web frontends or mobile applications).

## Requirements

- Python 3.x
- Django 3.x
- Django REST framework

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/online-store-inventory.git
    cd online-store-inventory
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Start the server**:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Inventory Items

- **GET /api/items/**: List all items.
- **POST /api/items/**: Create a new item.
- **GET /api/items/{id}/**: Retrieve an item by ID.
- **PUT /api/items/{id}/**: Update an item by ID.
- **DELETE /api/items/{id}/**: Delete an item by ID.

### Suppliers

- **GET /api/suppliers/**: List all suppliers.
- **POST /api/suppliers/**: Create a new supplier.
- **GET /api/suppliers/{id}/**: Retrieve a supplier by ID.
- **PUT /api/suppliers/{id}/**: Update a supplier by ID.
- **DELETE /api/suppliers/{id}/**: Delete a supplier by ID.

### Relationships

- **GET /api/items/{id}/suppliers/**: List all suppliers for a specific item.
- **GET /api/suppliers/{id}/items/**: List all items provided by a specific supplier.

## Testing the API with Postman

1. **Open Postman**.
2. **To create an item**:
    - Select `POST` method.
    - Enter URL: `http://127.0.0.1:8000/api/items/`
    - Set Headers: `Content-Type: application/json`
    - Set Body: Choose `raw` and `JSON` format. Enter the JSON:
    ```json
    {
        "name": "Item 1",
        "description": "Description 1",
        "price": 10.00,
        "supplier_ids": [1]
    }
    ```
    - Click `Send`.

3. **To create a supplier**:
    - Select `POST` method.
    - Enter URL: `http://127.0.0.1:8000/api/suppliers/`
    - Set Headers: `Content-Type: application/json`
    - Set Body: Choose `raw` and `JSON` format. Enter the JSON:
    ```json
    {
        "name": "Supplier 1",
        "contact_info": "Contact Info 1"
    }
    ```
    - Click `Send`.

4. **To list items or suppliers**:
    - Select `GET` method.
    - Enter URL: `http://127.0.0.1:8000/api/items/` or `http://127.0.0.1:8000/api/suppliers/`
    - Click `Send`.

## Documentation

- The API documentation provides detailed information on how to interact with the inventory and   supplier management system. Make sure to review the endpoint descriptions and request/response formats to effectively use the API.

- For further assistance, refer to the official Django and Django REST framework documentation.

---

- This `README.md` file covers the setup, API endpoints, and testing instructions using Postman, making it easier for anyone to understand and interact with your API.





