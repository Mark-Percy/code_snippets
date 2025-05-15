class Bookstore:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        book = {
            'title': title,
            'author': author,
            'price': price
        }
        self.books.append(book)

    def get_books(self):
        return self.books

    def find_book_by_title(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

    def find_books_by_author(self, author):
        return [book for book in self.books if book['author'] == author]

    
    def __str__(self):
        return "\n".join([f"{book['book']} - Quantity: {book['quantity']}" for book in self.books])

    def addBook(self, book, quantity=1):

        for k, bookstorage in enumerate(self.books):
            currBook = bookstorage['book']
            if currBook == book:
                self.books[k]['quantity'] += quantity
                return
        id = len(self.books) + 1
        self.books.append({'id': id,'book': book, 'quantity': quantity})
    
    def sellBook(self, id):
        for k, bookstorage in enumerate(self.books):
            if bookstorage['id'] == id:
                if bookstorage['quantity'] > 1:
                    self.books[k]['quantity'] -= 1
                else:
                    print(f"Book {bookstorage['book'].title} is out of stock")
                return
        



class Book:

    def __init__(self, title, author, price, edition=1):
        self.title = title
        self.author = author
        self.price = price
        self.edition = edition

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, edition: {self.edition}"
    
    def __eq__(self, value):
        if isinstance(value, Book):
            return self.title == value.title and self.author == value.author and self.edition == value.edition
        return NotImplemented


def main():
    bookstore = Bookstore()
    bookstore.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99))
    bookstore.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99))
    bookstore.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 2))
    bookstore.addBook(Book("1984", "George Orwell", 8.99), 2)
    print(bookstore)
    bookstore.sellBook(1)
    print('-'*80)
    print(bookstore)

main()
