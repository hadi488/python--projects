class Library:
    no_of_books = 3
    books = [['chemistry', 'jon doe'], ['physics', 'ionstion'], ['maths', 'newton']]
    # bookName = None
    # authorName = None
    def addbooks(self, bookname, authorname):
        self.bookName = bookname
        self.authorName = authorname
        self.book_name_and_author = [self.bookName , self.authorName]
        self.books.append(self.book_name_and_author)
        
    def deletebooks(self, bookname, authorname):
        self.bookName = bookname
        self.authorName = authorname
        self.book_name_and_author = [self.bookName , self.authorName]
        for book in self.books:
            if(self.bookName in book[0] and self.authorName in book[1]):
                self.books.remove(book)
                print('book deleted successfully')
        else:
            print('book not found')
                
    def updatebooks(self, bookname, authorname, updatebookname, updateauthorname):
        self.bookName = updatebookname
        self.authorName = updateauthorname
        self.book_name_and_author = [self.bookName , self.authorName]
        for book in range(len(self.books)):
            if(bookname in self.books[book][0] and authorname in self.books[book][1]):
                self.books[book] = self.book_name_and_author
                print('book updated successfully')
                break
        else:
            print('book not found')
                
    def showbooks(self):
        for book in self.books:
            print(f"{book[0]} by {book[1]}")
    
class arabicLibray(Library):
    pass

class EnglishLibrary(Library):
    pass


b1 = Library()

while True:
    print('enter your choice ')
    print('1 for add book')
    print('2 for delete book')
    print('3 for update book')
    print('4 for show books')
    print('5 for quit')
    choice = int(input("enter your choice "))

    match(choice):
        case 5:
            break
        case 1:
            bookname = input('enter book name to add')
            authorname= input('enter name of the author of that book')
            b1.addbooks(bookname, authorname)
        case 2:
            bookname = input('enter book name to delete')
            authorname= input('enter name of the author of that book')
            b1.deletebooks(bookname, authorname)
        case 3:
            bookname = input('enter book name to update')
            authorname= input('enter author name to update')
            updatebookname = input('enter new book name')
            updateauthorname= input('enter name of the author of that new book')
            b1.updatebooks(bookname, authorname, updatebookname, updateauthorname)
        case 4:
            b1.showbooks()
        case _:
            print("entered wrong choice")
    

    
