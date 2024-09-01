# Student library system

class Library:
    def __init__(self, listofbooks): # Constructor
        self.books = listofbooks 
        
    def displayAvailablebooks(self): # function
        print("Books present in this libarary are: ")
        for book in self.books:
            print("\t *" + book)
            
    def borrowbook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone else. Pleasse wait until the book is returned")
            return False
        
    def returnbook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")

class Student:
    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book
    
    def returnbook(self):
        self.book = input("Enter the name of the book you want to borrow")
        return self.book
    

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    #centralLibrary.displayAvailablebooks()
    while(True):
        welcomemsg = '''=====Welcome to central library=====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomemsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailablebooks()
        elif a == 2:
            centralLibrary.borrowbook(Student.requestbook())
        elif a == 3:
            centralLibrary.returnbook(Student.returnbook())
        elif a == 4:
            print("Thanks for choosing central library")
            exit()
        else:
            print("Invalid choice!")
            
            

