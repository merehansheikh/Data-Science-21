class Library_Item:
    def __init__(self, no, title, publisher):
        self.book_no = no
        self.title = title
        self.publisher = publisher
    def __str__(self):
        return f'Book Number: {self.book_no}\nTitle: {self.title}\n\nPublisher: {self.publisher}\n'

class Book(Library_Item):
    def __init__(self, no, title, author, publisher, edition):
        super().__init__(no, title, publisher)

        self.author = author
        self.edition = edition
    def __str__(self):
        return f'{super().__str__()}Author: {self.author}\nEdition:{self.edition}'

class ReferenceBook(Library_Item):
    def __init__(self, no, title, author, publisher, edition):
        super().__init__(no, title, publisher)

        self.author = author
        self.edition = edition
    def __str__(self):
        return f'{super().__str__()}Author: {self.author}\nEdition:{self.edition}\n*** Reference Book ***'

class Magazine(Library_Item):
    def __init__(self, no, title, author, publisher, month, year):
        super().__init__(no, title, publisher)

        self.month = month
        self.year = year
    def __str__(self):
        return f'{super().__str__()}Month: {self.month}\nYear:{self.year}'