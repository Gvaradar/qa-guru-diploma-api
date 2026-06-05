# API автотесты для диплома QA Guru

## Описание

Проект содержит API-тесты для тестового интернет-магазина [FakeStoreAPI](https://fakestoreapi.com/).

## Технологии

- Python 3.13
- pytest — тестовый фреймворк
- requests — HTTP-клиент
- allure-pytest — отчёты
- jsonschema — валидация JSON-схем

## Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/Gvaradar/qa-guru-diploma-api.git
cd qa-guru-diploma-api

### 2. Установить зависимости

pip install -r requirements.txt

### 3. Запустить тесты

pytest tests/ -v --alluredir=allure_results

### 4. Посмотреть Allure отчёт

allure serve allure_results

### 5. Настройка

Создайте файл `.env` в корне проекта и добавьте:

API_BASE_URL=https://fakestoreapi.com

### 6. Создать виртуальное окружение

python -m venv venv

source venv/bin/activate # для Linux/Mac

venv\Scripts\activate # для Windows

## Тесты

| Метод  | Эндпоинт    | Описание               |
|--------|-------------|------------------------|
| GET    | /products   | Получение всех товаров |
| GET    | /products/1 | Получение товара по ID |
| POST   | /products   | Создание нового товара |
| PUT    | /products/1 | Обновление товара      |
| DELETE | /products/1 | Удаление товара        |

## Логирование

- Консольное: дата, время, метод, URL, статус, тело ответа
- Allure: вложения с request и response

## Требования диплома

- ✅ 5 тестов (GET, POST, PUT, DELETE)
- ✅ Базовый URI в фикстуре
- ✅ Запросы через endpoint
- ✅ Схемы для request и response
- ✅ Allure и консольное логирование
- ✅ Валидация статуса, тела ответа, схемы