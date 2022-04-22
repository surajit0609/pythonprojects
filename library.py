from student import Student


class Library:
    def __init__(self,listofbooks,track):
        self.books=listofbooks
        self.track=track
    def display_books(self):
        for book in self.books:
            print(book,end=' ')
    def borrow_book(self,student,bookname):
        if student in self.track.keys() :
            print("sorry,you can not borrow a book")
        else:
            if bookname in self.books:
                print("recive this book")
                self.books.remove(bookname)
                self.track[student]=bookname
            else:
                print("this book is not available")    

    def return_book(self,bookname,student):
        print("thank you\n")
        self.books.append(bookname)
        self.track.pop(student)
    def donate_book(self,bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)            
            
              