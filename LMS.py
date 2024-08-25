import datetime
import os

class LMS:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        if not os.path.exists(self.list_of_books):
            with open(self.list_of_books, 'w') as bk:
                pass

        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id): {"Books_title": line.strip(), "lender_name": "", "Issue_date": "", "status": "available"}})
            Id += 1

    def display_books(self):
        print("--------------------List of Books-------------------")
        print("Books Id", "\t", "Title")
        print("----------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("Books_title"), "- [", value.get("status"), "]")

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == "available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books_dict[books_id]["status"] == "available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["status"] = "Already Issued"
                print("Book Issued Successfully!!!\n")
        else:
            print("Book ID not found!!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter Book title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("The character count is too long")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict)) + 1): {"Books_title": new_books, 'lender_name': "", 'Issue_date': "", "status": "available"}})
                print(f"This book '{new_books}' has been added successfully!!!")

    def return_books(self):
        books_id = input("Enter the books ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"] == "available":
                print("This book is already available in the library, Please check your ID")
                return self.return_books()
            elif not self.books_dict[books_id]["status"] == "available":
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['Issue_date'] = ""
                self.books_dict[books_id]["status"] = "available"
                print("Successfully Updated!!!")
        else:
            print("Book ID not found :(")

try:
    myLMS = LMS("list_of_books.txt", "Kawin's")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n----------------- Welcome to {myLMS.library_name} Library Management System --------------- \n")
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press Key: ").lower()
        if key_press == "i":
            print("\n Current Selection: Issue Books")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\n Current Selection: Add Books\n")
            myLMS.add_books()
        elif key_press == "d":
            print("\n Current selection: Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\n Current Selection: Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Please check your input:", e)
