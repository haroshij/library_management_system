from typing import Union


class Book:
    """Класс для создание экземпляров (книг)
    с указанием следующих данных: название,
    автор, год издания, статус (выдана или в наличии)."""

    # Инициализируем экзмепляр со всеми атрибутами.
    # ID книги считаем через статический метод класса.
    def __init__(self,
                 title: str = 'Название неизвестно',
                 author: str = 'Автор неизвестен',
                 year: Union[int, str] = 'Год написания неизвестен',
                 status: str = 'в наличии'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.id = Book.id_generetor(title, author, year)

    # Метод для генерации ID книги.
    @staticmethod
    def id_generetor(title: str, author: str, year: Union[int, str]):
        id = 0

        # ID получаем через сложение всех порядковых номеров символов
        # в таблице ASCII.
        for letter in title + author + str(year):
            id += ord(letter)
        return id


# Для тестирования корректности создания экземпляров.
if __name__ == '__main__':
    mumu = Book('Mu-mu', 'Turgenev', 1970)
    print(mumu.id)
