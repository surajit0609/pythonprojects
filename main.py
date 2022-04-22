from library import Library
from student import Student
s1=Student("23600121008",'cse',"1st")
s2=Student("23600121009",'cse',"1st")
l1=Library(['c','c++','python','java'],{s2:'q'})
l1.display_books()
l1.return_book('q',s2)
l1.display_books()
l1.borrow_book(s2,'c++')
l1.display_books()
