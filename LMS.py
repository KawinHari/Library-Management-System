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
            self.books_dict.update({str(Id):{"Books_title":line.replace("\n",""),"lender_name":"","Issue_date":"","status":"available"}})
            Id=Id+1

    def display_books(self):
        print("--------------------List of Books-------------------")
        print("Books Id","\t","Title")
        print("----------------------------------------------------")
        #
        for key,value in self.books_dict.items():
            print(key,"\t\t", value.get("Books_title"), "- [",value.get("status"),"]") 

    def Issue_books(self):
        books_id=input("Enter books ID: ")
        current_date=datetime.datetime.now().strftimie("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]["lender_name"]} on {self.books_dict[books_id]["Issue_date"]}")
                return self.Issue_books()
            elif self.books_dict[books_id]["status"]=="Available":
                your_name=input("enter your name: ")
                self.books_dict[books_id]["lender_name"]=your_name
                self.books_dict[books_id]["Issue_date"]=current_date
                self.books_dict[books_id]["status"]="Already Issued"
                print("Books Issued Successfully !!! \n")
        else:
            print("Book ID not found !!!")
            return self.Issue_books()
    
    def add_books(self):
        new_books=input("Enter Book title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books)>25:
            print("The charector is too long ")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{"books_title":new_books,"lender_name":"","Issue_date":"","status":"Available"}})
                



lms=LMS("list_of_books.txt","Python library")
print(lms.display_books())
