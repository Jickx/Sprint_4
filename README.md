# BooksCollector Tests

Этот репозиторий содержит тесты для класса `BooksCollector`.  
Тесты написаны с использованием `pytest`, с фикстурами и параметризацией.

## Установка зависимостей

1. Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
````

2. Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest -v
```

## Реализованные тесты

### Инициализация

* `test_books_collector_initial_state` — проверка начального состояния коллекции.

### Добавление книг

* `test_add_new_book_valid_length` — добавление книги с допустимой длиной имени.
* `test_add_new_book_invalid_length` — книги с недопустимой длиной имени не добавляются.
* `test_add_new_book_genre_is_empty` — новая книга без жанра имеет пустое значение.
* `test_add_new_book_duplicate_book` — одна и та же книга не добавляется дважды.

### Жанры

* `test_set_book_genre_valid_genre` — установка корректного жанра.
* `test_set_book_genre_invalid_genre` — установка несуществующего жанра невозможна.
* `test_get_book_genre_gets_genre_by_name` — получение жанра по имени книги.
* `test_get_books_with_specific_genre_includes_books_only_given_genre` — фильтрация книг по жанру.
* `test_get_books_genre_current_books_genre_dict` — словарь всех книг с жанрами.

### Книги для детей

* `test_get_books_for_children_gets_books_without_age_rating` — возвращаются только детские книги.
* `test_get_books_for_children_in_children_list_there_no_adult_books` — книги с возрастным рейтингом не попадают в
  детский список.

### Избранное

* `test_add_book_in_favorites_adds_book_in_favorites` — добавление книги в избранное.
* `test_add_book_in_favorites_same_book_not_duplicate` — книга не дублируется в избранном.
* `test_delete_book_from_favorites_deletes_book` — удаление книги из избранного.
* `test_get_list_of_favorites_books_returns_all` — возврат всех добавленных в избранное книг.

## Структура репозитория

```
├── books_collector.py # основной класс
├── test_books_collector.py # тесты
├── conftest.py # фикстуры
├── requirements.txt # зависимости
└── README.md # этот файл
```

