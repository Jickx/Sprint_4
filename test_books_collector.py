from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_books_collector_initial_state(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_adds_new_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1
        assert name in collector.books_genre

    def test_add_new_book_add_new_book_no_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_add_new_book_add_new_book_more_than_40_symbols(self, collector):
        name = 'Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_add_same_book_false(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1
        assert name in collector.books_genre


