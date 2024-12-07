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
    @staticmethod
    def format_price(price):
        return f"${price:.2f}"
    @classmethod
    def get_book_count(cls):
        return cls.book_count
book1 = Book("Python Programming","John Smith",29.99)
book1.display_info()
book1.set_price(39.99)
book1.display_info()
print(Book.get_book_count())
print(Book.format_price(39.99))

class EBook(Book):
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size
    def display_info(self):
        super().display_info()
        print("File Size:",self.file_size,"MB")

# ebook1 = EBook("Python Programming","John Smith",29.99,10)
# ebook1.display_info()
