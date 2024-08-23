import datetime
import os

class LMS:
    def __init__(self, list_of_books, library_name):
        self.list_of_books="list_of_books.txt"
        self.library_name=library_name
        self.books_dict={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readlines()
        for line in content:
            print(line)
print(LMS("list_of_books.txt","Python's Library"))