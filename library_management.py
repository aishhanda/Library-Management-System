import os
import csv
from datetime import datetime

file_name = "Library.csv"
file_path = os.path.abspath("Library.csv")

books = {
    "Power of Subconscious Mind" : True,
"The Psychology of Money" : True,
"Atomic Energy" : False,
"To Kill a Mockingbird" : True,
"The Alchemist" : True,
"Quantum Recipes for Teens" : False,
"1984" : True,
"Rich Dad Poor Dad" : True,
"Secrets of the Moonlight War" : False,
"Think and Grow Rich" : True
}

def run_csv():
        try:
            with open(file_name, mode='x', newline = '') as file:
                writer = csv.writer(file)
                writer.writerow(["Book Name", "Student Name", "class", "Returned/Borrowed", "Date"])
        except FileExistsError:
            pass


def activity_(book_name, student_name, which_class, action, date_time):
    with open(file_name, mode='a', newline='')as file:
        writer = csv.writer(file)
        writer.writerow([book_name, student_name, which_class, action, date_time.strftime("%D-%M-%Y %H:%M:%S")])



def add_book():
    new_book = input("Book Name: ")
    if new_book not in books:
        books[new_book] = True
        print(f'"{new_book}" has been added to the library and is marked available.')
    else:
        print(f'"{new_book}" is already in the library.')

def borrow_book():
    borrow = input("Book Name: ")
    if borrow in books.keys():
        if books[borrow]:
            student = input("Student name: ")
            class_ = input("Student's Class: ")
            books[borrow] = False
            print(f"Book has been borrowed!")
            activity_(borrow, student, class_, "Borrowed", datetime.now())

        else:
            print("Book not available!")
    else:
        print("\n⚠️ Book not found in the library.")

def return_book():
    return_ = input("Book name: ")
    books[return_] = True
    student = input("Student name: ")
    class_ = input("Student's Class: ")
    activity_(return_, student, class_, "Returned", datetime.now())


def display_books():
    for book in books:
        if books[book]:
            print(f"{book}: Available✅")
        else:
            print(f"{book}: Not Available❌")

def exit_():
    print("\n✅ All actions completed.")
    print(f"📁 Data saved successfully in:\n👉 {file_path}")
    print(f"'ctrl+click' on the url to open file or download file(RIGHT CLICK ON LIBRARY.CSV TO DOWNLOAD) and upload at excel:https://excel.cloud.microsoft/ to view the record")



run_csv()
while True:
        print("""
========= Library Menu =========
1. Add a new book
2. Borrow a book
3. Return a book
4. Display all books
5. Exit
================================
        """)
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("\nThank you for using the Library Management System.")
            exit_()
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")
