from typing import Union


class Book:

    id_dict = dict()
    unused_id = list(range(10_000, 100_000))

    def __init__(self, title='Название неизвестно', author='Автор неизвестен',
                 year='Год написания неизвестен', status='в наличии'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.id = Book.id_generetor(title, author, year)
        Book.id_dict[self.id] = f'{title}, {author}, {year}'

    @staticmethod
    def id_generetor(title: str, author: str, year: Union[int, str]):
        id = 0
        for letter in title + author + str(year):
            id += ord(letter)
        return id


# Для тестирования корректности создания экземпляров их методов.
if __name__ == '__main__':
    mumu = Book('Mu-mu', 'Turgenev', 1970)
    mumu2 = Book('Mu-mu', 'Turgenev', 1970)
    print(Book.id_dict)
    print(mumu.id)
