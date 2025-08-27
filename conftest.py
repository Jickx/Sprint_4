import pytest
from books_collector import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def add_one_book(collector):
    name = 'Гордость и предубеждение и зомби'
    collector.add_new_book(name)
    return name

@pytest.fixture
def add_one_book_with_genre(collector):
    name = 'Гордость и предубеждение и зомби'
    genre = 'Ужасы'
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    return name, genre

@pytest.fixture
def add_multiple_books(collector):
    books = [
        ['Гордость и предубеждение и зомби', 'Ужасы'],
        ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
        ['Анна Каренина против вампиров', 'Комедии'],
        ['Тихий Дон и громкая вечеринка', 'Мультфильмы']
    ]
    for name, genre in books:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return books

@pytest.fixture
def add_one_book_in_favorite(collector):
    name = 'Гордость и предубеждение и зомби'
    genre = 'Ужасы'
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    collector.add_book_in_favorites(name)
    return name, genre