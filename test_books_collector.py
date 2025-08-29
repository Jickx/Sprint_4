import pytest


class TestBooksCollector:

    def test_books_collector_initial_state(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name', ['A', 'A' * 15, 'A' * 40])
    def test_add_new_book_valid_length(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name', ['', 'A' * 41, 'A' * 100])
    def test_add_new_book_invalid_length(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_genre_is_empty(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    def test_add_new_book_duplicate_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1
        assert name in collector.books_genre

    def test_set_book_genre_valid_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.books_genre[name] = ''
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_set_book_genre_invalid_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Аниме'
        collector.books_genre[name] = ''
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    def test_get_book_genre_gets_genre_by_name(self, collector):
        name = 'Что делать, если ваш кот хочет вас убить'
        genre = 'Ужасы'
        collector.books_genre[name] = genre
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_gets_books_only_given_genre(self, collector):
        collector.books_genre = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы',
            'Анна Каренина против вампиров': 'Комедии',
            'Тихий Дон и громкая вечеринка': 'Мультфильмы'
        }
        result = collector.get_books_with_specific_genre('Ужасы')
        assert set(result) == {
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        }

    def test_get_books_genre_gets_current_books_genre_dict(self, collector):
        collector.books_genre = {
            'Гордость и предубеждение и зомби': ''
        }
        assert collector.get_books_genre() == {
            'Гордость и предубеждение и зомби': ''
        }

    def test_get_books_for_children_gets_books_without_age_rating(self, collector):
        collector.books_genre = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Детективы',
            'Анна Каренина против вампиров': 'Комедии',
            'Тихий Дон и громкая вечеринка': 'Мультфильмы'
        }
        assert set(collector.get_books_for_children()) == {
            'Анна Каренина против вампиров',
            'Тихий Дон и громкая вечеринка'
        }

    def test_get_books_for_children_in_children_list_no_adult_books(self, collector):
        collector.books_genre = {
            'Гордость и предубеждение и зомби': 'Ужасы',
            'Что делать, если ваш кот хочет вас убить': 'Детективы',
            'Анна Каренина против вампиров': 'Комедии',
            'Тихий Дон и громкая вечеринка': 'Мультфильмы'
        }
        adult_books = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]
        children_books = collector.get_books_for_children()
        for adult_book in adult_books:
            assert adult_book not in children_books

    def test_add_book_in_favorites_adds_book_in_favorites(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.books_genre[name] = ''
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_book_in_favorites_same_book_not_duplicate(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.books_genre[name] = ''
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1
        assert name in collector.favorites

    def test_delete_book_from_favorites_deletes_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.favorites.append(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books_returns_all(self, collector):
        collector.favorites = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить',
            'Анна Каренина против вампиров',
            'Тихий Дон и громкая вечеринка'
        ]
        assert set(collector.get_list_of_favorites_books()) == set(collector.favorites)
