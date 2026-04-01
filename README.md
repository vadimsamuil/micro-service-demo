# microservices-demo (Python + Flask + Docker Compose)

Учебный проект с двумя микросервисами:

- **user-service** — работает с пользователями
- **order-service** — работает с заказами и обращается к `user-service`

## Структура

```text
microservices-demo/
├── docker-compose.yml
├── README.md
├── user-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   └── users.json
└── order-service/
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py
    └── orders.json
```

## Что нужно установить

- Docker
- Docker Compose

## Запуск

```bash
docker compose up --build
```

## Проверка API

### 1. Получить всех пользователей

```bash
curl http://localhost:3001/users
```

### 2. Получить пользователя по ID

```bash
curl http://localhost:3001/users/1
```

### 3. Добавить пользователя

```bash
curl -X POST http://localhost:3001/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Charlie","email":"charlie@example.com"}'
```

### 4. Получить все заказы

```bash
curl http://localhost:3002/orders
```

### 5. Получить заказ с данными пользователя

```bash
curl http://localhost:3002/orders/1
```

### 6. Добавить заказ

```bash
curl -X POST http://localhost:3002/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"item":"Keyboard","amount":1}'
```

## Как работает взаимодействие сервисов

Когда вызывается:

```bash
GET /orders/1
```

`order-service`:

1. читает `orders.json`
2. находит заказ
3. делает HTTP-запрос в `user-service` по адресу:
   `http://user-service:3001/users/<user_id>`
4. возвращает заказ вместе с данными пользователя

## Остановка

```bash
docker compose down
```
