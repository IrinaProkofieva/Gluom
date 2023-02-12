# Gluom
## Как запустить: 
1. Клонируем гит-репозиторий
2. В корне проекта docker-compose up

В результате поднимется сервис и база данных, заполненная данными.
Порт: 5000

## API
**GET** `/ping`
Возвращает 200;Ok

**GET** `/api/list`
**params:** 
`size` - int, min_val=1, required=true
`page` - int, min_val=1, required=true
Запрос с пагинацией. Возвращает список всех данных о еде

Формат возвращаемых данных:
```
{
  "cur_page": , //текущая страница
  "items": [
    {
      "carbohydrate": , //углеводы
      "fat":  , //жиры
      "kcal":  , //килокалории
      "name": , //название блюда
      "protein": //белки
    }
  ],
  "total_pages":  //общее число страниц
}
```

**GET** `/api/search`
**params:** 
`size` - int, min_val=1, required=true
`page` - int, min_val=1, required=true
`text` - string, required=true - текст для поиска в бд
Запрос с пагинацией. Возвращает список данных по введенному тексту

Формат ответа аналогичен предыдущему endpoint-у.

**Пример запроса:**
`http://127.0.0.1:5000/api/search?text=пюре&page=1&size=2`

**Пример ответа:**
```
{
  "cur_page": 1,
  "items": [
    {
      "carbohydrate": 11.0,
      "fat": 3.0,
      "kcal": 90.0,
      "name": "Йогуртное пюре Gerber с грушей и бананом",
      "protein": 1.0
    },
    {
      "carbohydrate": 12.0,
      "fat": 2.2,
      "kcal": 70.0,
      "name": "Йогуртное пюре Gerber с малиной и черникой",
      "protein": 0.8
    }
  ],
  "total_pages": 72
}
```

