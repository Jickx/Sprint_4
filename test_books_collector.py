class TestBooksCollector:

    def test_books_collector_initial_state(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_saves_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1
        assert name in collector.get_books_genre()

    def test_add_new_book_sets_empty_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_add_new_book_name_41_symbols_not_added(self, collector):
        name = 'Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_same_book_not_duplicated(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert name in collector.books_genre
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid_genre_set(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_do_nothing_if_book_exists_and_genre_not_exists(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Аниме'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_gets_genre_if_book_exists(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == 'Ужасы'

    def test_get_books_with_specific_genre_includes_books_only_given_genre(
            self, collector
    ):
        books = [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Анна Каренина против вампиров', 'Комедии'],
            ['Тихий Дон и громкая вечеринка', 'Мультфильмы']
        ]
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]

    def test_get_books_genre_gets_current_dict_with_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    def test_get_books_for_children_gets_gets_books_without_rating(self, collector):
        books = [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
            ['Анна Каренина против вампиров', 'Комедии'],
            ['Тихий Дон и громкая вечеринка', 'Мультфильмы']
        ]
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == [
            'Анна Каренина против вампиров',
            'Тихий Дон и громкая вечеринка'
        ]

    def test_get_books_for_children_no_adult_books_in_children_list(self, collector):
        books = [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
            ['Анна Каренина против вампиров', 'Комедии'],
            ['Тихий Дон и громкая вечеринка', 'Мультфильмы']
        ]
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        for name, genre in books:
            if genre in collector.genre_age_rating:
                assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_adds_book_in_favorites(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_same_book_not_duplicate(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_deletes_book(self, collector):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_all(self, collector):
        books = [
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы'],
            ['Анна Каренина против вампиров', 'Комедии'],
            ['Тихий Дон и громкая вечеринка', 'Мультфильмы']
        ]
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
            collector.add_book_in_favorites(name)

        assert set(collector.get_list_of_favorites_books()) == set([_[0] for _ in books])

