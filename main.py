import json

class Book:
    def __init__(self, author="", title="", pages=0, year=0 ):
        self.author = author
        self.title = title
        self.pages = pages 
        self.year = year 
        
    # если захотите посмотреть содержимое списка
    def __repr__(self):
        return f"Book(author={self.author}, title={self.title}, pages={self.pages}, year={self.year})"
    
    def to_dict(self):
        return {
            "author": self.author,
            "title": self.title,
            "pages": self.pages,
            "year": self.year
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["author"], data["title"], data["pages"], data["year"])

        
class BookManager:
    
    def __init__(self):
        self.books = []
        self.count = 0
        
    def isPositiveNumber(self, value):
        return value > 0
        
    def showMenu(self) -> int:
        print("Меню:")
        print("1. Добавить запись.")
        print("2. Загрузить данные из файла.")
        print("3. Сохранить данные в файл.")
        print("4. Удалить запись.")
        print("5. Показать все книги.")
        print("6. Отсортировать книги по названию.")
        print("7. Отсортировать книги по страницам.")
        print("8. Отсортировать книги по году издания.")
        print("9. Выход")
        choice = input("Введите номер пункта: ")
        return choice
    
    def displayBooks(self):
        if self.count == 0:
            print("Список книг пуст.")
            return ""

        # Заголовки таблицы
        print(f"{'№':<4} | {'Автор':<12} | {'Название книги':<18} | {'Страницы':<15} | {'Год':<5}")
        print("-" * 80)

        # Вывод данных
        for i, book in enumerate(self.books, start=1):
            print(f"{i:<4} | {book.author:<12} | {book.title:<18} | {book.pages:<15} | {book.year:<5}")

        # Разделитель после таблицы
        print("-" * 80)

    def saveToFile(self, filename):
        try:
            books_data = [book.to_dict() for book in self.books]
    
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(books_data, file, indent=4, ensure_ascii=False)
            print(f"Данные сохранены в файл {filename}.")
        except Exception as e:
            print(f"Ошибка сохранения в JSON: {e}")
                          
    def loadFile(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                books_data = json.load(file)
                self.books += [Book.from_dict(data) for data in books_data]
                self.count = len(self.books)
            print(f"Данные загружены из файла {filename}.")
        except Exception as e:
            print(f"Ошибка открытия файла {e}!")
            self.count = len(self.books)
                    
    def addBook(self):
        # ввод автора
        author = input("Введите автора книги: ")
        # ввод названия 
        title = input("Введите название книги: ")
        
        # ввод страниц
        while True:
            try:
                pages = int(input("Введите кол-во страниц: "))
                if self.isPositiveNumber(pages):
                    break
                else:
                    print("Введите положительное значение!")
            except ValueError as a:
                print(f"Ошибка {a}, введите числовое значение!")
        # ввод года
        while True:
            try:
                year = int(input("Введите год издания: "))
                if self.isPositiveNumber(year):
                    break
                else:
                    print("Введите положительное значение!")
            except ValueError as a:
                print(f"Ошибка {a}, введите числовое значение!")
        
        self.books.append(Book(author, title, pages, year))
        self.count += 1
        print("Книга добавлена!")
        
    def deleteBook(self):
        try: 
            if len(self.books) == 0:
                return "Список книг пуст!"
            self.displayBooks()
            print(f"Введите номер книги для удаления (от 1 до {self.count}).")
            index = int(input("Введите номер книги: "))
            if 1 <= index <= self.count:
                del self.books[index - 1]
                self.count -= 1
                print("Книга успешно удалена!")
            else:
                print("Введите правильный номер книги!")
        except ValueError:
            print("Введите числовое значение!")
            
    def sortTitle(self):
        self.books.sort(key=lambda book: book.title)
        print("Книги отсортированны по названию!")
        
    def sortYear(self):
        self.books.sort(key=lambda book: book.year)
        print("Книги отсортированны по году издания!")
        
    def sortPages(self): 
        self.books.sort(key=lambda book: book.pages)
        print("Книги отсортированны по страницам!")
          
def main():
    filename = "data.json"
    
    bookManager = BookManager()
    try:
        while True:
            choice = bookManager.showMenu()
        
            if choice == "1": bookManager.addBook()
            elif choice == "2": bookManager.loadFile(filename)
            elif choice == "3": bookManager.saveToFile(filename)
            elif choice == "4": bookManager.deleteBook()
            elif choice == "5": bookManager.displayBooks()
            elif choice == "6": bookManager.sortTitle()
            elif choice == "7": bookManager.sortPages()
            elif choice == "8": bookManager.sortYear()
            elif choice == "9": 
                print("Выход из программы.")
                break
            else:
                print("Ошибка! Введите верный пункт меню.")
    except KeyboardInterrupt:
        print(" - Немедленное завершение программы!")
            
            
if __name__ == "__main__":
    main()