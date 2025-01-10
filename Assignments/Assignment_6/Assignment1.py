class BookStore:
    NoOfBooks = 0  # Class variable
    
    def __init__(self, name, author):
        self.Name = name  # Instance variable
        self.Author = author  # Instance variable
        BookStore.NoOfBooks += 1  # Increment the class variable
    
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()  

Obj2 = BookStore("Some Book", "Some Author")
Obj2.Display()  
