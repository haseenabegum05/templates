import tkinter as tk
from tkinter import messagebox

class LibraryGUI:
    def __init__(self, window):
        self.window = window
        self.library = Library(["vistas", "invention", "rich&poor", "indian", "macroeconomics", "microeconomics"])
        self.student = Student()
        self.track = []

        self.window.title("Delhi Library")

        self.label_title = tk.Label(self.window, text="WELCOME TO THE HAZENA LIBRARY", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.label_choice = tk.Label(self.window, text="Choose an option:")
        self.label_choice.pack()

        self.btn_list_books = tk.Button(self.window, text="List Available Books", command=self.displayAvailableBooks)
        self.btn_list_books.pack(pady=5)

        self.frame_borrow = tk.Frame(self.window)
        self.frame_borrow.pack(pady=5)

        self.label_name = tk.Label(self.frame_borrow, text="Name:")
        self.label_name.pack(side=tk.LEFT)

        self.entry_name = tk.Entry(self.frame_borrow)
        self.entry_name.pack(side=tk.LEFT)

        self.label_book = tk.Label(self.frame_borrow, text="Book:")
        self.label_book.pack(side=tk.LEFT)

        self.entry_book = tk.Entry(self.frame_borrow)
        self.entry_book.pack(side=tk.LEFT)

        self.btn_borrow = tk.Button(self.window, text="Borrow Book", command=self.borrowBook)
        self.btn_borrow.pack(pady=5)

        self.frame_return = tk.Frame(self.window)
        self.frame_return.pack(pady=5)

        self.label_name_return = tk.Label(self.frame_return, text="Name:")
        self.label_name_return.pack(side=tk.LEFT)

        self.entry_name_return = tk.Entry(self.frame_return)
        self.entry_name_return.pack(side=tk.LEFT)

        self.label_book_return = tk.Label(self.frame_return, text="Book:")
        self.label_book_return.pack(side=tk.LEFT)

        self.entry_book_return = tk.Entry(self.frame_return)
        self.entry_book_return.pack(side=tk.LEFT)

        self.btn_return = tk.Button(self.window, text="Return Book", command=self.returnBook)
        self.btn_return.pack(pady=5)

        self.frame_donate = tk.Frame(self.window)
        self.frame_donate.pack(pady=5)

        self.label_book_donate = tk.Label(self.frame_donate, text="Book:")
        self.label_book_donate.pack(side=tk.LEFT)

        self.entry_book_donate = tk.Entry(self.frame_donate)
        self.entry_book_donate.pack(side=tk.LEFT)

        self.btn_donate = tk.Button(self.window, text="Donate Book", command=self.donateBook)
        self.btn_donate.pack(pady=5)

        self.btn_track_books = tk.Button(self.window, text="Track Borrowed Books", command=self.trackBooks)
        self.btn_track_books.pack(pady=5)

        self.btn_exit = tk.Button(self.window, text="Exit Library", command=self.exitLibrary)
        self.btn_exit.pack(pady=5)

    def displayAvailableBooks(self):
        messagebox.showinfo("Available Books", "\n".join(self.library.books))

    def borrowBook(self):
        name = self.entry_name.get()
        bookname = self.student.requestBook()
        self.library.borrowBook(name, bookname)

    def returnBook(self):
        bookname = self.student.returnBook()
        self.library.returnBook(bookname)

    def donateBook(self):
        bookname = self.student.donateBook()
        self.library.donateBook(bookname)

    def trackBooks(self):
        if len(self.track) > 0:
            book_info = "\n".join([f"{list(item.values())[0]} book is taken/issued by {list(item.keys())[0]}." for item in self.track])
            messagebox.showinfo("Borrowed Books", book_info)
        else:
            messagebox.showinfo("Borrowed Books", "No books are issued.")

    def exitLibrary(self):
        self.window.destroy()


class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        pass

    def borrowBook(self, name, bookname):
        pass

    def returnBook(self, bookname):
        pass

    def donateBook(self, bookname):
        pass


class Student:
    def requestBook(self):
        pass

    def returnBook(self):
        pass

    def donateBook(self):
        pass


if __name__ == "__main__":
    window = tk.Tk()
    library_gui = LibraryGUI(window)
    window.mainloop()
