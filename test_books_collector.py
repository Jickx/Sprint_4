import pytest


class TestBooksCollector:

    def test_books_collector_initial_state(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('add_one_book', ['A', 'A' * 15, 'A' * 40], indirect=True)
    def test_add_new_book_valid_length(self, add_one_book, collector):
        assert add_one_book in collector.get_books_genre()

    @pytest.mark.parametrize('add_one_book', ['', 'A' * 41, 'A' * 100], indirect=True)
    def test_add_new_book_invalid_length(self, add_one_book, collector):
        assert add_one_book not in collector.get_books_genre()

    @pytest.mark.parametrize('add_one_book', ['Гордость и предубеждение и зомби'], indirect=True)
    def test_add_new_book_genre_is_empty(self, add_one_book, collector):
        assert collector.get_book_genre(add_one_book) == ''

    def test_add_new_book_duplicate_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert name in collector.books_genre
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('add_one_book_with_genre', [('Гордость и предубеждение и зомби', 'Ужасы')], indirect=True)
    def test_set_book_genre_valid_genre(self, add_one_book_with_genre, collector):
        name, genre = add_one_book_with_genre
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('add_one_book_with_genre', [('Гордость и предубеждение и зомби', 'Аниме')], indirect=True)
    def test_set_book_genre_invalid_genre(self, add_one_book_with_genre, collector):
        name, genre = add_one_book_with_genre
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize('add_one_book_with_genre', [('Что делать, если ваш кот хочет вас убить', 'Ужасы')],
                             indirect=True)
    def test_get_book_genre_gets_genre_by_name(self, add_one_book_with_genre, collector):
        name, genre = add_one_book_with_genre
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('add_multiple_books', [[
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ('Анна Каренина против вампиров', 'Комедии'),
        ('Тихий Дон и громкая вечеринка', 'Мультфильмы')
    ]], indirect=True)
    def test_get_books_with_specific_genre_includes_books_only_given_genre(self, add_multiple_books, collector):
        result = collector.get_books_with_specific_genre('Ужасы')
        assert set(result) == {'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'}

    @pytest.mark.parametrize('add_one_book', ['Гордость и предубеждение и зомби'], indirect=True)
    def test_get_books_genre_current_books_genre_dict(self, add_one_book, collector):
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    @pytest.mark.parametrize('add_multiple_books', [[
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ('Анна Каренина против вампиров', 'Комедии'),
        ('Тихий Дон и громкая вечеринка', 'Мультфильмы')
    ]], indirect=True)
    def test_get_books_for_children_gets_books_without_age_rating(self, add_multiple_books, collector):
        assert set(collector.get_books_for_children()) == {
            'Анна Каренина против вампиров',
            'Тихий Дон и громкая вечеринка'
        }

    @pytest.mark.parametrize('add_multiple_books', [[
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ('Анна Каренина против вампиров', 'Комедии'),
        ('Тихий Дон и громкая вечеринка', 'Мультфильмы')
    ]], indirect=True)
    def test_get_books_for_children_in_children_list_there_no_adult_books(self, add_multiple_books, collector):
        children_books = collector.get_books_for_children()
        for name, genre in add_multiple_books:
            if genre in collector.genre_age_rating:
                assert name not in children_books

    @pytest.mark.parametrize('add_one_book', ['Гордость и предубеждение и зомби'], indirect=True)
    def test_add_book_in_favorites_adds_book_in_favorites(self, add_one_book, collector):
        name = add_one_book
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('add_one_book', ['Гордость и предубеждение и зомби'], indirect=True)
    def test_add_book_in_favorites_same_book_not_duplicate(self, add_one_book, collector):
        name = add_one_book
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('add_one_book', ['Гордость и предубеждение и зомби'], indirect=True)
    def test_delete_book_from_favorites_deletes_book(self, add_one_book, collector):
        name = add_one_book
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('add_multiple_books', [[
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
        ('Анна Каренина против вампиров', 'Комедии'),
        ('Тихий Дон и громкая вечеринка', 'Мультфильмы')
    ]], indirect=True)
    def test_get_list_of_favorites_books_returns_all(self, add_multiple_books, collector):
        books = add_multiple_books
        for name, _ in books:
            collector.add_book_in_favorites(name)
        assert set(collector.get_list_of_favorites_books()) == {name for name, _ in books}
