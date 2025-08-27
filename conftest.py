import pytest
from books_collector import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def add_one_book(request, collector):
    name = request.param
    collector.add_new_book(name)
    return name


@pytest.fixture
def add_one_book_with_genre(request, collector):
    name, genre = request.param
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    return name, genre


@pytest.fixture
def add_multiple_books(request, collector):
    for name, genre in request.param:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return request.param
