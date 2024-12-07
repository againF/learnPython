class Book:
    book_count=0
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.__price=price
        Book.book_count+=1
    def display_info(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.__price)
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        if new_price>0:
            self.__price=new_price
        else:
            print("Invalid price")
        return self
    @staticmethod
    def format_price(price):
        return f"${price:.2f}"
    @classmethod
    def get_book_count(cls):
        return cls.book_count


class EBook(Book):
    ebook_count=0
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size
        EBook.ebook_count+=1
    def display_info(self):
        super().display_info()
        print("File Size:",self.file_size,"MB")
    
    @classmethod
    def get_ebook_count(cls):
        return cls.ebook_count
    def download(self):
        print(f"Downloading ebook {self.title}...")
class PrintedBook(Book):
    def __init__(self, title, author, price, pages):
        super().__init__(title, author, price)
        self.pages = pages
    def display_info(self):
        super().display_info()
        print(f"页数：{self.pages}")

def display_book_info(book):
    book.display_info()


book1 = Book("Python Programming","John Smith",29.99)
# book1.display_info()
# book1.set_price(39.99).display_info()
# print(Book.format_price(39.99))
ebook1 = EBook("Python Programming","John Smith",29.99,10)
printedBook1 = PrintedBook("PrintedBook","John Smith",29.99,10)
# ebook1.display_info()
# print(Book.get_book_count())
# print(EBook.get_ebook_count())
# display_book_info(book1)
# print("-" * 30)
# display_book_info(ebook1)
# print("-" * 30)
# display_book_info(printedBook1)
ebook1.download()
ebook1.set_price(-1)
