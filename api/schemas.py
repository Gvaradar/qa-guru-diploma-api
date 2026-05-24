product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"}
    },
    "required": ["id", "title", "price", "description", "category", "image"]
}

products_list_schema = {
    "type": "array",
    "items": product_schema
}
# Схема для валидации request (создание товара)
product_request_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 1},
        "price": {"type": "number", "minimum": 0},
        "description": {"type": "string", "minLength": 1},
        "category": {"type": "string"},
        "image": {"type": "string"}
    },
    "required": ["title", "price", "description", "category"]
}